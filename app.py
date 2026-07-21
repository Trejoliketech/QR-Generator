from flask import Flask, send_file, request, render_template, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import qrcode
import os
import uuid
import io

os.makedirs("static", exist_ok=True)

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "30 per hour"]
)

@app.route("/", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def home():
    data = request.form.get("data")
    if data: #Checks to make sure something was submitted
        data = data.strip()#strips away empty white spaces
        if data and len(data) <= 4096: #Checks to make sure data is still present and is less than 4096 characters
            return render_template("index.html", image_ready=True, qr_data=data)
    return render_template("index.html", image_ready=False)

def generate_qr(data):
    qr = qrcode.QRCode (
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    return buffer

@app.route("/qr-image")
@limiter.limit("10 per minute")
def qr_image():
    data = request.args.get("data")
    if not data:
        abort(400)
    data = data.strip()
    if not data or len(data) > 4096:
        abort(400)
    buffer = generate_qr(data)
    return send_file(buffer, mimetype = "image/jpeg")
    
if __name__ == "__main__":
    app.run(debug=False)