import csv
import os

# 比較するcsvファイルの数
num_files = 144

# csvファイルのパス
file_paths = []
for i in range(num_files):
    prefix = f"new_{i:02d}"
    if i == 0:
        suffix = "00.csv"
        file_paths.append(f"/Users/soso/Dropbox/データ分析/10m_new/02new/{prefix}:00:00.csv")
        for j in range(1, 6):
            suffix = f"{j}0:00.csv"
            file_paths.append(f"/Users/soso/Dropbox/データ分析/10m_new/02new/{prefix}:{suffix}")
    else:
        for j in range(0, 6):
            suffix = f"{j}0:00.csv"
            file_paths.append(f"/Users/soso/Dropbox/データ分析/10m_new/02new/{prefix}:{suffix}")

# 抽出したデータを保存する新しいcsvファイルのパス
output_path = "/Users/soso/Downloads/02new_new_000000~235000.csv"

# SPSの列のインデックスを取得
with open(file_paths[0], "r") as file1:
    reader1 = csv.reader(file1)
    header1 = next(reader1)
    sps_col_indices = [header1.index("SPS") for _ in range(num_files)]  # SPS列のインデックスを取得

# セルA、B列が一致している行を抽出する
matching_rows = []
with open(file_paths[0], "r") as file1:
    reader1 = csv.reader(file1)
    header1 = next(reader1)
    for row1 in reader1:
        instance_type = row1[0]
        az = row1[1]
        sps_values = []
        for i in range(num_files):
            with open(file_paths[i], "r") as file2:
                reader2 = csv.reader(file2)
                header2 = next(reader2)
                for row2 in reader2:
                    if row1[0] == row2[0] and row1[1] == row2[1]:
                        sps_values.append(row2[sps_col_indices[i]])
                        break
                file2.seek(0)
        matching_rows.append([instance_type, az] + sps_values)

# 抽出したデータを新しいcsvファイルとして保存する
with open(output_path, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["InstanceType", "AvailabilityZone"] + [f"SPS{i}" for i in range(1, num_files + 1)])
    writer.writerows(matching_rows)
