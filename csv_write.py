import csv
print("start")
"""
with open('output.csv', 'a', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(['課名', '成績', '排名'])

  # 寫入另外幾列資料
  
  writer.writerow(['令狐沖', 175, [1,2,3]])
  writer.writerow(['岳靈珊', 165, 57])
"""
# 開啟 CSV 檔案
with open('output.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  row = list(rows)
  print(row[4][2])