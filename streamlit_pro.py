import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm
from io import StringIO
from PIL import Image

import numpy as np
import mouse
import keyboard

from PIL import Image
import requests
from io import BytesIO

import plotly.graph_objects as go
import plotly.express as px

'''
def keyboard_down(evt):
     if evt.name == 'enter':
          print('{}'.format(evt.name))
          print("save! 2")
# curser 조건문
if True:
     keyboard.on_press(keyboard_down)
'''

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers

st.title("LMNOP 회의록 서비스")
# st.subheader("스트림 스트림")

# ---------- 사이드바 화면 구성 --------------------

st.sidebar.title("음성 목록")
st.sidebar.header("녹음 파일 선택")
selectbox_options = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인'] # 셀렉트박스의 선택 항목
your_option = st.sidebar.selectbox('좋아하는 작품은?', selectbox_options, index=3) # 셀렉트박스의 항목 선택 결과
st.sidebar.write('**당신의 선택**:', your_option)

user_id = st.sidebar.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value="abcd", type="password")



folder = './data/'

audio_file = './data/재즈.mp3' # 오디오 파일 경로
# audio_local = open(audio_file, 'rb')
# audio_bytes = audio_local.read()
        
# 녹음 제목
user_id = st.text_input('음성 제목 입력', value="streamlit", max_chars=20)
title_save_clicked = st.button('저장')
if title_save_clicked:
     print("save!")

# 녹음 파일 업로드
uploaded_file = st.file_uploader("회의록을 작성할 녹음 파일을 선택하세요.", type='mp3')
if uploaded_file is not None:
     # 음성 분석하기
     print()
    # 바이너리 파일을 읽어서 바이트로 변환
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data[:100]) # 일부의 내용 출력
download_clicked = st.button('다운로드')
if download_clicked:
     # 파일 다운로드

     with open(folder + "녹음 파일.txt", encoding='utf-8') as text_file:
          text_data = text_file.read()
          st.download_button(
                    label="텍스트 파일 다운로드", 
                    data = text_data, 
                    file_name="서연의_이야기.txt"
     )