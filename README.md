# AutoMM

## 실행방법

1. 깃헙 클론
2. 가상환경 설정
3. 노션을 참고하여 .env 파일, api key 파일을 구성
4. docker-compose up

```bash

git clone https://github.com/2024-summer-LLM-Bootcamp/AutoMM.git

python3 -m venv venv
# 가상환경 켜기 (windows)
source venv/Scripts/activate

pip install -r requirements.txt

# .env 파일 작성

streamlit run app.py
```
