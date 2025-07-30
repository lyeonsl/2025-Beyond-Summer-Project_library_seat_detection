import os
import shutil

partial_dir = "C:/Users/user/Downloads/도서관 사진-20250723T040543Z-1-001/도서관 사진"
full_dir = "C:/Users/user/Downloads/도서관 사진-20250730T083524Z-1-002/도서관 사진"
output_dir = "C:/Users/user/Downloads/도서관 사진-라벨링_추가할_누락이미지/도서관 사진"

valid_ext = ('.jpg', '.jpeg', '.png', '.webp', '.heic')

# 파일 목록 불러오기 (strip + 확장자 필터)
partial_images = set(f.strip() for f in os.listdir(partial_dir) if f.lower().endswith(valid_ext))
full_images = set(f.strip() for f in os.listdir(full_dir) if f.lower().endswith(valid_ext))

missing_images = full_images - partial_images

print(f"라벨링 중 이미지 개수 (partial): {len(partial_images)}")
print(f"전체 이미지 개수 (full): {len(full_images)}")
print(f"누락 이미지 개수: {len(missing_images)}")

# 누락 이미지 샘플 출력
if missing_images:
    print("누락된 이미지 샘플:", list(missing_images)[:5])
else:
    print("누락된 이미지가 없습니다. 파일명이 같은 것으로 판단됩니다.")

# 누락 이미지 복사
if missing_images:
    os.makedirs(output_dir, exist_ok=True)
    for fname in missing_images:
        src_path = os.path.join(full_dir, fname)
        dst_path = os.path.join(output_dir, fname)
        shutil.copy2(src_path, dst_path)
    print(f"복사 완료: {output_dir} 에 총 {len(missing_images)}개 이미지 저장됨")
else:
    print("복사할 이미지가 없습니다.")

