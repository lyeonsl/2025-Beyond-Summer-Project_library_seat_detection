from PIL import Image
import os
import pillow_heif  # HEIC 지원
pillow_heif.register_heif_opener()

input_folder = "C:/Users/user/Downloads/도서관 사진-라벨링_추가할_누락이미지/도서관 사진"
output_folder = "C:/Users/user/Downloads/도서관 사진-누락이미지_jpg변환/도서관 사진"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.heic')):
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                img = img.convert("RGB")
                new_name = os.path.splitext(filename)[0] + ".jpg"
                save_path = os.path.join(output_folder, new_name)
                img.save(save_path, "JPEG", quality=95)
        except Exception as e:
            print(f"오류 발생: {filename} → {e}")

print("JPG 변환 완료 (HEIC 포함)")
