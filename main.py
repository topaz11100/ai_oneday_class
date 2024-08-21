import streamlit as st
import openaiapi

st.title('제품 홍보 포스터 생성기')

text_promft = "를 팔아야하는 세일즈맨이라고 생각하며 300바이트 이내의 솔깃한 제품 홍보 문구를 작성해줘. 줄바꿈해서 출력해줘"

keyword = st.text_input("키워드 입력",
                        label_visibility='hidden',
                        placeholder="키워드를 입력하세요.")

if st.button('생성 :fire:'):
  with st.spinner('생성 중입니다.'):
    st.image(openaiapi.image_url_return(keyword))
    st.write(openaiapi.text_return(keyword + text_promft))
