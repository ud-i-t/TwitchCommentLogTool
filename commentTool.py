import json
import os
import sys

# 必要な情報を抽出して表示する関数
def extract_twitch_message_info(data):
    user_data = data['data']
    
    # 表示名、コメント、日時の抽出
    display_name = user_data['displayName']
    comment = user_data['comment']
    timestamp = user_data['timestamp']

    print(f"{timestamp[:10]} {display_name}: {comment}")

# ログフォルダを指定
arguments = sys.argv
folder = arguments[1]
file_list = os.listdir(folder)

while True:
    name = input("検索したいユーザのscreenNameを入力してください:")

    for file_name in file_list:
        # ファイルを読み込み、1行ずつ表示
        with open(f'{folder}\{file_name}', 'r', encoding='utf-8') as file:
            for line in file:
                parsed_data = json.loads(line.strip())
                if parsed_data['service'] != 'twitch':
                    continue

                user_data = parsed_data['data']
                if name in user_data['screenName']:
                    extract_twitch_message_info(parsed_data)

    print("------------------------------------\n")
