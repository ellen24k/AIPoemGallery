import streamlit as st

from pkg_utils.utils import menu_hide
from pkg_views import login, menu

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        menu.load_view()
    else:
        login.load_view()


if __name__ == '__main__':
    menu_hide()
    main()
