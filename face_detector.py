import cv2
import sys

def detect_faces(image_path):
    # Загружаем каскадный классификатор для обнаружения лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Читаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return

    # Преобразуем изображение в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Находим лица на изображении
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Выводим результат
    print(f"Found {len(faces)} face(s) in the image.")

    # Отображаем координаты найденных лиц
    for (x, y, w, h) in faces:
        print(f"Face at [{x}, {y}, {w}, {h}]")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "test_image.jpg"
    detect_faces(image_path)
