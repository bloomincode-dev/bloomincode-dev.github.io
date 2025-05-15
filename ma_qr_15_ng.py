import csv
import requests
import os
import re
import unicodedata

template = "pRM72Bw"  # Template của Mon
save_folder = "./qr_mon_users/"

# Hàm chuyển tiếng Việt có dấu -> không dấu + an toàn tên file
def slugify(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '_', text)

# Tạo thư mục nếu chưa có
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
        safe_name = slugify(name)  # Chuyển tên thành không dấu + snake_case
        filename = f"{save_folder}{safe_name}_{acc}.png"

        with open(filename, "wb") as f:
            f.write(img_data)

        print(f"✅ QR cho {name} đã lưu: {filename}")