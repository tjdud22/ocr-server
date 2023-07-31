from PIL import Image
import pytesseract

# Tesseract OCR 경로 설정 (Tesseract가 설치된 경로로 변경해주세요)
pytesseract.pytesseract.tesseract_cmd = r'C:\leeseoyoung\workspace\tesseract.exe'

# 이미지 파일을 불러옴
image_path = r'C:\Users\Administrator\Desktop\test.png'
image = Image.open(image_path)

# 이미지에서 글씨 추출
extracted_text = pytesseract.image_to_string(image, lang='eng')  # 'eng'은 영어 언어를 사용한다는 의미

# 추출된 텍스트 출력
print(extracted_text)