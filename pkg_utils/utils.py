from datetime import datetime

import requests
import streamlit as st
import streamlit.components.v1 as components

# streamlit_app
def menu_hide():
    # .stAppToolbar {visibility: hidden;}
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stToolbarActionButton {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# about, admin, chatbot, gallery, login
def padding_set():
    css = """
    <style>
    .stMainBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 {
        padding-top: 48px;
        padding-right: 4px;
        padding-bottom: 4px;
        padding-left: 4px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def extract_filename(url):
    start = url.rfind('/') + 1
    # end = url.find('?', start)
    # if start != 0 and end != -1:
    if start != 0:
        return url[start:]
    return None


# chatbot
def read_version(file_path='version.txt'):
    with open(file_path, 'r') as file:
        version = file.read().strip()
    return version

# def get_current_time_no_spaces():
#     cur_time = datetime.now()
#     return cur_time.strftime('%Y%m%d%H%M%S%f')

def get_current_time_no_spaces():
    cur_time = datetime.now()
    return (cur_time.strftime('%Y-%m-%d %H:%M:%S.%f'), cur_time.strftime('%Y%m%d%H%M%S%f'))

def autoplay_audio(file_path):
    audio_html = f"""
    <audio autoplay style="display:none;">
      <source src="{file_path}" type="audio/wav">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)


def download_file(url, destination_file):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(destination_file, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f'파일이 {url}에서 {destination_file}(으)로 다운로드 되었습니다.')

def scroll_here():
    html_code = """
                        <div id="scroll-target" style="margin-top: 1000px;"></div>
                        <script>
                          function scrollToTarget() {
                            document.getElementById('scroll-target').scrollIntoView({ behavior: 'smooth' });
                          }
                          window.onload = scrollToTarget;
                        </script>
                    """

    components.html(html_code, height=0)