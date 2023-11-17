import openai
from openai import OpenAI


def create_new_conversation(selected_api_key):
    openai.api_key = selected_api_key
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=selected_api_key,
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
