from openpyxl import Workbook
import json

# 엑셀파일 쓰기
write_wb = Workbook()

# 이름이 있는 시트를 생성
# sheet = write_wb.create_sheet('no name')

# Sheet1에다 입력
sheet = write_wb.active

# 데이터 불러오기
headers = ['category', 'mAP', 'mAP_50', 'mAP_75', 'mAP_s', 'mAP_m', 'mAP_l']
sheet.append(headers) 


with open('test_json.json', 'r') as rf:
    data = json.load(rf) 
    sorted_data = sorted(data, key=lambda x: x['category'][-2:])

for d in sorted_data:
    new_data = list(d.values())
    sheet.append(new_data) 

# #셀 단위로 추가
# sheet.cell(5, 5, '5행5열')

write_wb.save("test2.xlsx")