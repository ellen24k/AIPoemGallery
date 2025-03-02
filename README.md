# AI 삼행시 갤러리 v2.0 2025
### 프로젝트 소개
- - -
> _**AI 삼행시 갤러리**_ 는 사용자가 제시한 단어를 기반으로 삼행시와 삼행시에 기반한 이미지, 시 낭송 음성을 생성합니다.

(v1.0) Azure Speech(TTS), Dall-e3, Chat-GPT4
with GitHub, Streamlit, Supabase(Storage, PostgreSQL, Edge Function), Azure AI Studio and GitHub Action Deploy, SQL & PLpgSQL routines(stored procedure) with pg_net extension, Trigger, TypeScript, Python, Docker, Langchain, pyshorteners, npm, pip, requests, dot-env, thread, async.. 등등 다양한 api를 활용해 개발했습니다.

(v2.0) Streamlit 사이트에서 작동하던 앱을 Oracle Cloud로 이전하였습니다. Supabase의 Storage, PostgreSQL, Edge Fucntion를 Minio Object Storage, Python Apscheduler로 변경하였습니다. 또한 Jenkins를 적용하여 이미지를 자동빌드 및 배포하게 CI/CD를 변경하였습니다.
## _**AI 삼행시 갤러리**_ v1.0~v2.0
- - -
AI를 활용한 삼행시 생성 및 삼행시 기반 이미지 생성기
> v1.0 프로젝트 기간: `2024.11~2024.12`
> \
> v2.0 프로젝트 기간: `2025.1~2025.2`
> \
> [Github Repo](https://github.com/ellen24k/AIPoemGallery/)

### 주요 기능
- - -
- 삼행시 생성
    - 사용자가 세 글자 단어를 입력하면 해당 글자를 이용해 삼행시와, 삼행시에 어울리는 그림을 생성할 수 있다.
- 갤러리
    - 지금까지 생성한 삼행시, 음성 파일 및 그림을 확인할 수 있다.
- 갤러리 관리
    - 관리자는 생성된 삼행시 자료들을 삭제할 수 있다.