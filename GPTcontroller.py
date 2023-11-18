import os
import openai
from openai import OpenAI
import json


def create_new_conversation(selected_api_key):
    openai.api_key = selected_api_key
    messages = []
    marker = input("What type of chatbot you want me to be?")
    messages.append({"role": "system", "content": marker})
    print("Alright!Our conversion will about {marker}" + "\n" + "You can now type your messages."
                                                                "Enter '!quit' to stop.")
    while True:
        message = input("")
        if message.lower() == '!quit':
            break
        messages.append({"role": "user", "content": message})
        client = OpenAI(
            api_key=selected_api_key,
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(reply)
    print("Conversation ended.")
    save_conversation(messages, marker)


def load_conversation_by_marker(selected_api_key, marker, conversation_directory="conversations"):
    filename = f"conversation_{marker}.json"
    full_file_path = os.path.join(conversation_directory, filename)

    if os.path.exists(full_file_path):
        with open(full_file_path, 'r') as file:
            messages = json.load(file)
            print("Let's continue the conversation!What's your problem now?"+"\n"+":")
            while True:
                message = input("")
                if message.lower() == '!quit':
                    break
                messages.append({"role": "user", "content": message})

                client = OpenAI(
                    api_key=selected_api_key,
                )
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-1106",
                    messages=messages
                )
                reply = response.choices[0].message.content
                messages.append({"role": "assistant", "content": reply})
                print(reply)
            print("Conversation ended.")
            save_conversation(messages, marker, conversation_directory)
    else:
        print(f"No conversation found with marker {marker}")


def save_conversation(messages, marker, conversation_directory="conversations"):
    if marker:
        filename = f"conversation_{marker}.json"
    else:
        filename = "conversation_new.json"

    # 获取当前工作目录并构建相对路径
    current_directory = os.getcwd()
    full_directory_path = os.path.join(current_directory, conversation_directory)

    # 创建目录，如果不存在
    os.makedirs(full_directory_path, exist_ok=True)

    # 构建完整的文件路径
    file_path = os.path.join(full_directory_path, filename)

    try:
        with open(file_path, 'w') as file:
            json.dump(messages, file, indent=4)
        print(f"Conversation saved to {file_path}")
    except Exception as e:
        print(f"Error: {e}")


def display_all_markers(conversation_directory="conversations"):
    # 获取当前工作目录并构建相对路径
    current_directory = os.getcwd()
    full_directory_path = os.path.join(current_directory, conversation_directory)

    # 列出目录中的所有文件
    files = [f for f in os.listdir(full_directory_path) if f.endswith(".json")]

    # 遍历每个文件并显示文件名（包含 marker）
    for file in files:
        # 从文件名中提取 marker
        marker = file.split("_")[1].split(".json")[0]
        print(f"Marker in file {file}: {marker}")
