import os
from openai import AzureOpenAI
import streamlit as st
from openai import AzureOpenAI

# 환경 변수 설정
str_api_key = os.getenv("AZURE_OPENAI_API_KEY")
str_api_version = os.getenv("OPENAI_API_VERSION")
str_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(
    api_key=str_api_key,  # Azure Open AI Key
    api_version=str_api_version,  # Azue OpenAI API model
    azure_endpoint=str_endpoint  # Azure Open AI end point(매직에꼴)
)

# 음성 인식 함수


def transcribe_audio(audio_file_path):
    audio_file = open(audio_file_path, "rb")
    transcript = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper",
        language="ko",
        response_format="text",
        temperature=0.0,
    )
    print(transcript)
    return transcript


# 요약 함수
def summarize_text(text):
    client = AzureOpenAI(
        api_key=str_api_key,  # Azure Open AI Key
        api_version=str_api_version,  # Azue OpenAI API model
        azure_endpoint=str_endpoint  # Azure Open AI end point(매직에꼴)
    )
    template = """
당신은 텍스트 요점 정리 함수이며, 반환값은 반드시 JSON 데이터여야 합니다.
STEP별로 작업을 수행하면서 그 결과를 아래의 출력 결과 JSON 포맷에 작성하세요.
STEP-1. 아래 세 개의 백틱으로 구분된 텍스트를 원문 그대로 읽어올 것
STEP-2. 텍스트를 개조식으로 요약하세요. 
개조식 요약의 정의는 다음과 같다.:
소제목
1. 내용
2. 내용
3. 내용
...

소제목
1. 내용
2. 내용
3. 내용
...

다음의 말투로 번역할 것:["지구의 나이는 45억 살이다.", "세종대왕은 조선의 위대한 국왕이다."]
```{text}```
---
출력 결과: {{"STEP-1": <입력텍스트>의 첫 50글자,  "STEP-2": <text를 요점 정리 결과>}} 
"""

    template = template.format(text=text)

    context = [{"role": "user", "content": template}]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=context,
        temperature=0,
        top_p=0,
        seed=1234
    )
    summary = response.choices[0].message.content
    print(summary)
    # llm = OpenAI(api_key=openai.api_key)
    # prompt = PromptTemplate(
    #     input_variables=["text"],
    #     template="Please summarize the following meeting transcript:\n\n{text}"
    # )
    # chain = LLMChain(llm=llm, prompt=prompt)
    # summary = chain.run(text=text)
    return summary


# Streamlit 앱 설정
st.title("Automatic Meeting Transcript and Summarization")
st.write("Upload an audio file to transcribe and summarize the meeting.")

# 파일 업로드 받기
uploaded_file = st.file_uploader("Choose an audio file...", type=["wav"])

if uploaded_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 음성 인식 (음성 파일을 텍스트로 변환)
    transcript = transcribe_audio("temp_audio.wav")
    st.subheader("Meeting Transcript")
    st.text_area("Transcript", transcript, height=300)

    # 텍스트 요약
    if st.button("Summarize Transcript"):
        summary = summarize_text(transcript)
        st.subheader("Summary")
        st.text_area("Summary", summary, height=150)
