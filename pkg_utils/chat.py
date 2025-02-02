from langchain_openai import AzureChatOpenAI
import os


def make_poem(user_input):
    chat_model = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY_EASTUS"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION_EASTUS_GPT4"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_EASTUS_GPT4")
    )
    user_input_reformat = f"'{user_input[0]}' '{user_input[1]} '{user_input[2]}'"
    messages = [
        {'role': 'system', 'content': 'You\'re a poet with a lot of sensibility.'},
        {'role': 'system', 'content': f'The output format must be \'{user_input[0]}\': content \'{user_input[1]}\': content \'{user_input[2]}\': content'},
        {'role': 'user', 'content': f'{user_input_reformat} 3글자로 3행시 만들어.'}
    ]
    print(messages)
    result = chat_model.invoke(input=messages)
    return result.content