FROM python:3.11

# Устанавливаем системные библиотеки для PySide6/Qt
RUN apt-get update && apt-get install -y \
    libgl1 \
    libegl1 \
    libglib2.0-0 \
    libxkbcommon0 \
    libfontconfig1 \
    libdbus-1-3 \
    libxcb-cursor0 \
    libx11-xcb1 \
    libxcb1 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-render-util0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-randr0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-xinput0 \
    libxcb-xkb1 \
    libxkbcommon-x11-0 \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

CMD ["python", "app/run_gui.py"]