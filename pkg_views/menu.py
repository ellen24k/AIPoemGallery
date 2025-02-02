import streamlit as st
from streamlit_option_menu import option_menu

from pkg_views import chatbot, gallery, admin, about


def load_view():
    options = ['ChatBot', 'Gallery', 'About', 'Admin']

    menu_style = {
        "container": {"width:": "100%", "display": "flex", "justify-content": "space-between",
                      "padding": "0!important"},
        "icon": {"color": "white", "font-size": "1.5em"},
        "nav-link": {"color": "white", "font-size": "1.0em", "padding": "0 0.5em", "text-decoration": "none",
                     "--hover-color": "grey"},
        "nav-link-selected": {"color": "white", "font-size": "1.0em", "padding": "0 0.5em", "text-decoration": "none"},
    }

    selected_option = option_menu(
        menu_title=None,
        options=options,
        icons=['robot', 'image', 'book', 'lock'],
        orientation='horizontal',
        styles=menu_style,
    )

    if 'admin' not in st.session_state:
        st.session_state['admin'] = False

    # Options
    if selected_option == 'ChatBot':
        chatbot.load_view()
    elif selected_option == 'Gallery':
        gallery.load_view()
    elif selected_option == 'Admin':
        admin.load_view()
    else:
        about.load_view()