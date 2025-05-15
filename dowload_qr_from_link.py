import requests

# Link ảnh QR từ VietQR
url = "https://api.vietqr.io/image/970415-113366668888-pRM72Bw.jpg?amount=0"

# Gửi GET request để tải ảnh
response = requests.get(url)

# Lưu ảnh QR về máy
with open("mon_qr_vietqr.png", "wb") as f:
    f.write(response.content)

print("✅ Ảnh QR đã được lưu: mon_qr_vietqr.png")