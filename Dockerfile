# 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

# 환경 변수 설정을 docker-compose.yml에서 처리하므로 Dockerfile에서 설정할 필요가 없습니다

# Streamlit 앱 실행
CMD ["streamlit", "run", "app.py"]
