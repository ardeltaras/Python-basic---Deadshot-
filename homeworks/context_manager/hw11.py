
print("# TASK 1")
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE
import datetime

class custom_file_manage():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.file = open(file_name, mode)
        with open('logs.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} {self.file_name} OPEN\n")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('logs.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} {self.file_name} CLOSE\n")
        self.file.close()

# Для перевірки datetime open та close для запису та читання файлу
with custom_file_manage('write_read.txt', 'w+') as f:
    f.write(f"{datetime.datetime.now()} WRITTEN TEXT\n")
    f.seek(0)
    print(f"{f.read()}{datetime.datetime.now()} REDDING TEXT\n")

with open('logs.txt', 'r') as logs_txt:
    logs_txt.seek(0)
    print(logs_txt.read())


print("# TASK 2")
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE
import csv

def txt_to_csv():
    with open('logs.txt', 'r') as f_txt:
        lines = (line.split() for line in f_txt)
        with open('logs.csv', 'w') as f_csv:
            writer = csv.writer(f_csv)
            writer.writerows(lines)

txt_to_csv()
with open('logs.csv', 'r') as f_csv:
    print(f_csv.read())


print("# TASK 3 (з зірочкою)")
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }
import json

def csv_to_json():
    with open('logs.csv', 'r') as csv_f:
        reader = csv.reader(csv_f, delimiter=',')
        rowcount = 0
        for bloc in reader:
            if bloc[3] == 'OPEN':
                rowcount += 1
                dict = {bloc[2]: {"count": None, "last_time_opened": f''}}
                dict[bloc[2]]["count"] = rowcount
                dict[bloc[2]]["last_time_opened"] = f'{bloc[0]} {bloc[1]}'
    with open('logs.json', 'w') as json_f:
        json.dump(dict, json_f, indent=4)

csv_to_json()
with open('logs.json', 'r') as json_f:
    print(json_f.read())
