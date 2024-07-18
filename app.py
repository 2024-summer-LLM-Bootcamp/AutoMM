import os
import openai
import streamlit as st
from google.cloud import speech
import io
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate

# 환경 변수 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 음성 인식 함수


def transcribe_audio(audio_file_path):
    # client = speech.SpeechClient()

    # with io.open(audio_file_path, "rb") as audio_file:
    #     content = audio_file.read()

    # audio = speech.RecognitionAudio(content=content)
    # config = speech.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=16000,
    #     language_code="en-US",
    # )

    # response = client.recognize(config=config, audio=audio)

    # transcript = ""
    # for result in response.results:
    #     transcript += result.alternatives[0].transcript

    # return transcript
    pass

    # LangChain을 이용한 텍스트 처리 및 요약 함수


def summarize_text(text):
    # llm = OpenAI(api_key=openai.api_key)
    # prompt = PromptTemplate(
    #     input_variables=["text"],
    #     template="Please summarize the following meeting transcript:\n\n{text}"
    # )
    # chain = LLMChain(llm=llm, prompt=prompt)
    # summary = chain.run(text=text)
    # return summary

    # Streamlit 앱 설정
    pass


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
