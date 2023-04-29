import csv
import os

# 新しいファイル名から始まる84個のcsvファイルを読み込む
num_files = 84
folder_path = "/Users/soso/Downloads/10m_new/31new/"
file_paths = []
for i in range(9, 24):
    prefix = f"new_{i:02d}"
    for j in range(6):
        suffix = f"{j*10:02d}:00.csv"
        file_path = os.path.join(folder_path, prefix + ":" + suffix)
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            file_paths.append(file_path)

# 以下、元のプログラムと同じです
output_path = "/Users/soso/Downloads/31new_new_000000~235000.csv"
with open(file_paths[0], "r") as file1:
    reader1 = csv.reader(file1)
    header1 = next(reader1)
    sps_col_indices = [header1.index("SPS") for _ in range(num_files)]

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

with open(output_path, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["InstanceType", "AvailabilityZone"] + [f"SPS{i}" for i in range(1, num_files + 1)])
    writer.writerows(matching_rows)
