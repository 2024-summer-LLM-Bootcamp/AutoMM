import streamlit as st
import datetime as dt
from pytz import timezone

from streamlit_jupyter import StreamlitPatcher, tqdm
from io import StringIO
from PIL import Image

import numpy as np

from PIL import Image
import requests
from io import BytesIO

import plotly.graph_objects as go
import plotly.express as px

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers
folder = './data/'
N = 0
# ---------- 사이드바 화면 구성 --------------------
st.sidebar.title("음성 목록")
selectbox_options = ['장작.mp3'] # 셀렉트박스의 선택 항목
your_option = st.sidebar.selectbox('녹음 파일 선택', selectbox_options) # 셀렉트박스의 항목 선택 결과

# ---------- 메인 화면 구성 --------------------
st.title("LMNOP 회의록 서비스")
tab1, tab2, tab3 = st.tabs(["업로드", "편집", "회의 요약"])

# 업로드 탭
with tab1:
     st.subheader("회의록 제목")
     current_time = dt.datetime.now(timezone('Asia/Seoul'))
     ampm_dict = {
          'AM': '오전',
          'PM': '오후'
     }
     formatted_time = current_time.strftime("%Y년 %m월 %d일") + ' ' + ampm_dict[current_time.strftime("%p")] + ' ' + current_time.strftime("%I:%M")
     st.text(formatted_time)

     title_save_clicked = st.button('저장')
     if title_save_clicked:
          print("save!")

     # 녹음 파일 업로드
     st.subheader('참석자')
     st.text('김수연 이하람')
     st.subheader('음성기록')
     
     # uploaded_file = st.file_uploader("녹음 파일을 업로드해주요.", type='mp3')
     # if uploaded_file is not None:
     #     N += 1
          # 음성 분석하기
     #     print("음성 분석")
          
     uploaded_file = st.file_uploader("텍스트 파일을 업로드해주요.", type='txt')
     if uploaded_file is not None:
          N += 1
          # 음성 분석하기
          print("텍스트 분석")
          
# 편집 탭
with tab2:
     st.subheader("회의록 제목")
     current_time = dt.datetime.now(timezone('Asia/Seoul'))
     ampm_dict = {
          'AM': '오전',
          'PM': '오후'
     }
     formatted_time = current_time.strftime("%Y년 %m월 %d일") + ' ' + ampm_dict[current_time.strftime("%p")] + ' ' + current_time.strftime("%I:%M")
     st.text(formatted_time)

     txt_minutes = st.text_area(label="회의록", label_visibility="collapsed", placeholder="회의록 내용입니다.")

     edit_clicked = st.button('편집')
     if edit_clicked:
          print()

# 회의 요약 탭
with tab3:
     st.subheader("회의록 제목")
     current_time = dt.datetime.now(timezone('Asia/Seoul'))
     ampm_dict = {
          'AM': '오전',
          'PM': '오후'
     }
     formatted_time = current_time.strftime("%Y년 %m월 %d일") + ' ' + ampm_dict[current_time.strftime("%p")] + ' ' + current_time.strftime("%I:%M")
     st.text(formatted_time)

     
     [col1, col2] = st.columns(2)
     with col1:
          txt_minutes2 = st.text_area(label="회의", placeholder="회의록 내용입니다.")
     with col2:
          txt_summary = st.text_area(label="요약",placeholder="회의 요약 내용입니다.")
     
     [col3, col4] = st.columns([0.9, 0.1])
     with col4:
          summary_clicked = st.button('요약')
          if title_save_clicked:
               print("summary!")
               
     [col5, col6, col7] = st.columns([0.4, 0.2, 0.4])
     if uploaded_file is not None:
          uploaded_data = uploaded_file.getvalue()
          st.write(uploaded_data) 
          stringio = StringIO(uploaded_data.decode("utf-8"))
          string_data = stringio.read()
          f = open("회의-{}.txt", 'bw') # 파일 열기(바이너리 파일 쓰기 모드)
          f.write(string_data)  # 파일에 이미지 데이터 쓰기
          f.close()      # 파일 닫기

     with col6:
          folder = './data/'
          with open(folder + "서연의_이야기.txt", encoding='utf-8') as text_file:
               text_data = text_file.read()
               st.download_button(
                         label="다운로드", 
                         data = text_data, 
                         file_name="회의-{}.txt".format(N))
          