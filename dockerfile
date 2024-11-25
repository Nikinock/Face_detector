# Базовый образ Python
FROM python:3.8-slim AS builder

# Установка инструментов сборки
RUN apt-get update && \
    apt-get install -y cmake g++ wget unzip libgtk2.0-dev

# Скачиваем и распаковываем исходники OpenCV
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.3.zip && \
    unzip opencv.zip && \
    mkdir -p opencv-4.5.3/build

# Собираем OpenCV
WORKDIR /opencv-4.5.3/build
RUN cmake .. && \
    make -j$(nproc) && \
    make install

# Сборка основного образа
FROM python:3.8-slim
COPY --from=builder /usr/local /usr/local

WORKDIR /app
COPY face_detector.py /app
COPY test_image.jpg /app

ENTRYPOINT ["python", "face_detector.py"]
