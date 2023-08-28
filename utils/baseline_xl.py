from openpyxl import Workbook
import json


# 엑셀파일 쓰기
write_wb = Workbook()

# Sheet1에다 입력
sheet = write_wb.active

# 데이터 불러오기
headers = ['category', 'mAP', 'mAP_50', 'mAP_75', 'mAP_s', 'mAP_m', 'mAP_l']
sheet.append(headers) 

with open('baseline_mAP.json', 'r') as rf:
    data = json.load(rf)
    data = list(data.items())
    sorted_data = sorted(data, key=lambda x: x[0][-2:])
    print(sorted_data)

for row_idx, d in enumerate(sorted_data, start=2):
    cat = d[0]
    mAP_data = list(d[1].values())

    new_data = mAP_data
    new_data.insert(0, cat) # list

    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for col_idx, elem in zip(alphabet, new_data):
        sheet[f"{col_idx}{row_idx}"] = elem

write_wb.save("baseline_mAP.xlsx")