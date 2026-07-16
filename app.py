from flask import Flask, send_file, request, render_template
import qrcode
import os

os.makedirs("static", exist_ok=True)

app = Flask(__name__)

@app.route("/")
def home():
    data = request.args.get("data")
    if data:#Checks to make sure there is actual data within the user submitted url
        generate_qr(data, "static/output.jpg")
        return render_template("index.html", image_ready=True)
    else:
        return render_template("index.html", image_ready=False)
    

def generate_qr(data, filename):
    qr = qrcode.QRCode (
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(filename)   
    
# @app.route("/generate")
# def generate_function():
#     data=request.args.get("data")
#     generate_qr(data, "output.jpg")
#     return send_file("output.jpg")

if __name__ == "__main__":
    app.run(debug=True)