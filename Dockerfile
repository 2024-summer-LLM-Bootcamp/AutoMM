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

# 필요한 패키지들을 복사하고 설치
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# 앱 파일 복사
COPY . .

# 환경 변수 설정을 docker-compose.yml에서 처리하므로 Dockerfile에서 설정할 필요가 없습니다

# Streamlit 앱 실행
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
