import streamlit as st
import os

from pkg_utils.utils import padding_set

def load_view():
    padding_set()
    st.title('AI 삼행시 갤러리')
    password = st.text_input('입장코드를 입력하세요.')
    correct_password = os.getenv('ENTER_PASSWORD')

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.button('입장'):
        if password == correct_password:
            st.success('성공')
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error('입장코드가 틀렸습니다.')
    st.divider()