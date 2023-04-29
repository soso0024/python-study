import os
import pandas as pd
import shutil

# フォルダ内のCSVファイルのリストを取得します
folder_path = '/Users/soso/Downloads/10m/28'
file_list = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 新しいフォルダを作成します
new_folder_path = '/Users/soso/Downloads/28new'
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# すべてのCSVファイルについて処理を繰り返します
for file in file_list:
    # CSVファイルを読み込みます
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    # 不要な列の名前を指定します
    unwanted_columns = ['SpotPrice', 'Region', 'OndemandPrice', 'IF', 'Savings']

    # 指定した列を削除します
    df = df.drop(columns=unwanted_columns)

    # 新しいCSVファイルに保存するためのパスを作成します
    new_file_path = os.path.join(new_folder_path, 'new_' + file)

    # 新しいファイルを保存する前に、同じ名前のファイルが存在している場合は削除する
    if os.path.exists(new_file_path):
        os.remove(new_file_path)

    # 新しいファイルに保存します
    df.to_csv(new_file_path, index=False)

# 新しいフォルダにすべてのCSVファイルを移動します
for file in file_list:
    file_path = os.path.join(new_folder_path, 'new_' + file)
    shutil.move(file_path, new_folder_path)

