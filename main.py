import os
import openai

import GPTcontroller
import api_key_manager
from GPTcontroller import create_new_conversation

if __name__ == '__main__':
    api_key_manager.set_api_key("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", "user1")
    # 显示所有标识供用户选择
    api_key_manager.display_identifiers()
    print("[A]dd API key | [Q]uit")
    user_choice = input("Enter choice: ").lower()

    if user_choice == 'a':
        api_key_manager.add_api_key()
    elif user_choice == 'q':
        pass
    else:
        selected_api_key = api_key_manager.get_api_key(user_choice)
        if selected_api_key:
            openai.api_key = selected_api_key
            print(f"Using API key for {user_choice}")
            if api_key_manager.test_api_key(selected_api_key):
                print("Successfully logged in...")
                choose = input("enter !new to create new conversation or !load to load existing conversation: ")
                if choose == '!new':
                    GPTcontroller.create_new_conversation(selected_api_key)
                elif choose == '!load':
                    GPTcontroller.display_all_markers()
                    marker = input("Please enter marker: ")
                    GPTcontroller.load_conversation_by_marker(selected_api_key, marker)
            else:
                print("API key test failed. Please check the key or network.")
        else:
            print("Invalid choice or API key not found")
