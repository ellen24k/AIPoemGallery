import streamlit as st

from pkg_utils.utils import padding_set


def load_view():
    padding_set()

    st.write(
        '''
        # AI 삼행시 갤러리
        created by: 김태영
        - - -
        ### using Dall-e-3, Chat-GPT4'''
    )
