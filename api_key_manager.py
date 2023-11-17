import openai
from openai import OpenAI
from GPTcontroller import create_new_conversation

api_key_dict = {}  # 用来存储API密钥和对应标识的字典


def set_api_key(api_key, identifier):
    # 将新的API密钥添加到字典中
    api_key_dict[identifier] = api_key


def display_identifiers():
    # 在命令行中显示所有的标识
    print("Available identifiers:")
    for identifier in api_key_dict:
        print(f"- {identifier}")


def get_api_key(identifier):
    # 根据标识从字典中获取相应的API密钥
    return api_key_dict.get(identifier, None)


def add_api_key():
    # 在命令行中添加新的API密钥和标识
    new_identifier = input("Enter the new identifier: ")
    new_api_key = input("Enter the new API key: ")
    set_api_key(new_api_key, new_identifier)
    print(f"Added API key for {new_identifier}")


def test_api_key(selected_api_key):
    # 在这个函数中执行一个测试，验证API密钥是否有效
    # 这可能包括向API发出一个简单的请求来验证密钥
    # 在这里你可以自定义验证API密钥的逻辑
    openai.api_key = selected_api_key
    try:
        # 使用 OpenAI API 的一个简单请求来测试 API 密钥
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
            model="gpt-3.5-turbo-1106",
        )
        # 如果请求成功，说明 API 密钥有效
        return True
    except openai.error.AuthenticationError:
        # 如果遇到验证错误，说明 API 密钥无效
        return False