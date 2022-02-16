import qrcode
import base64
import io

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    s = io.BytesIO()
    img = qr.make_image(fill='black', back_color='white')
    img.save(s, format='PNG')
    s2 = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")

    return [{"type": "image", "data":  {"alt": "QR code", "src": "data:image/png;base64, " + s2}}]
