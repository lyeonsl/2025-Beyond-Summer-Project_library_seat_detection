from PIL import Image
import os

input_folder = "C:/Users/user/Downloads/도서관 사진-누락이미지_jpg변환/도서관 사진"
output_folder = "C:/Users/user/Downloads/도서관 사진-누락이미지_jpg회전/도서관 사진"

# 출력 폴더 없으면 생성
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        rotated = img.rotate(+90, expand=True)  # 시계방향 90도 회전
        save_path = os.path.join(output_folder, filename)
        rotated.save(save_path)
