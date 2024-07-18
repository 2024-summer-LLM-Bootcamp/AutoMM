from langchain.chains import SimpleChain
from langchain.llms import OpenAI
import streamlit as st

from google.cloud import speech
import io


def transcribe_audio(audio_file_path):
    """
    google STT
    """
    client = speech.SpeechClient()
    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, sample_rate_hertz=16000,
        language_code="en-US")

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript


def summarize_text(text):
    """
    AI 요약
    """
    llm = OpenAI(api_key="YOUR_OPENAI_API_KEY")
    chain = SimpleChain(llm=llm)

    prompt = f"Please summarize the following meeting transcript:\n\n{text}"
    summary = chain.run(prompt)

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
