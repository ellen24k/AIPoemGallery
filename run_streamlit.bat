@REM start "C:\Program Files (x86)\Google\Chrome\Application\chrome" https://azureopenaichatbotweb-eqbdxzpg3qqrctguzxaw2a.streamlit.app/
@REM streamlit run main_web.py --server.port 8501 --server.runOnSave true
call env-vars.bat
streamlit run streamlit_app.py --server.runOnSave true