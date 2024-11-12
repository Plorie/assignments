import cv2
import numpy as np

# 노란색 및 흰색 필터의 HSV 범위 설정
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

white_lower = np.array([0, 0, 200])
white_upper = np.array([180, 30, 255])

# 이미지 처리 함수
def process_image(img_path):
    # 이미지 읽기 및 크기 조정
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (640, 480))  # 필요 시 크기 조정

    # BGR을 HSV로 변환
    hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)

    # 노란색과 흰색 마스크 생성
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask_white = cv2.inRange(hsv, white_lower, white_upper)

    # 검은 배경을 가진 이미지 생성
    combined_image = np.zeros_like(img_resized)

    # 노란색 영역 표시
    combined_image[mask_yellow > 0] = [0, 255, 255]  # 노란색 (BGR)

    # 흰색 영역 표시
    combined_image[mask_white > 0] = [255, 255, 255]  # 흰색 (BGR)

    return combined_image

# 이미지 처리 및 결과 저장
image_paths = ["/home/gudtn7866/embedded/week10/images/line_tracer_images/1.jpg", "/home/gudtn7866/embedded/week10/images/line_tracer_images/2.jpg", "/home/gudtn7866/embedded/week10/images/line_tracer_images/3.jpg", "/home/gudtn7866/embedded/week10/images/line_tracer_images/4.jpg"]
output_images = []
output_folder = "/home/gudtn7866/embedded/week10/output_images/"

for i, img_path in enumerate(image_paths):
    processed_image = process_image(img_path)
    output_images.append(processed_image)
    file_path = f"{output_folder}processed_image_{i+1}.jpg"
    cv2.imwrite(file_path, processed_image)  # 지정된 폴더에 저장


# 결과 보기 (선택사항)
for i, processed_image in enumerate(output_images):
    cv2.imshow(f"Processed Image {i+1}", processed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()