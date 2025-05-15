import csv
import requests
import os

template = "pRM72Bw"  # Thay bằng template QR của Mon
save_folder = "./qr_mon_users/"

# Tạo thư mục lưu ảnh nếu chưa có
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Đọc file CSV
with open("maqr_15ng.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        name = row["name"]
        acc = row["account"]
        acqId = row["acqId"]
        amount = row["amount"]
        message = row["message"]

        # Tạo link QR từ VietQR API
        qr_url = f"https://api.vietqr.io/image/{acqId}-{acc}-{template}.jpg?amount={amount}&addInfo={message}"

        # Tải ảnh QR
        img_data = requests.get(qr_url).content
        filename = f"{save_folder}{name.replace(' ', '_')}_{acc}.png"

        with open(filename, "wb") as f:
            f.write(img_data)

        print(f"✅ QR cho {name} đã lưu: {filename}")