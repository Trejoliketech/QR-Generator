from flask import Flask, send_file, request
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    return "<form action='/generate' method='GET'><input type='text' name ='data'><button type='submit'>Generate</button></form>"

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
    
@app.route("/generate")
def generate_function():
    data=request.args.get("data")
    generate_qr(data, "output.jpg")
    return send_file("output.jpg")

if __name__ == "__main__":
    app.run(debug=True)