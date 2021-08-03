#this is a modal
import os
import csv
# 要檢查的檔案路徑
filepath = "./output.csv"

# 檢查檔案是否存在
if os.path.isfile(filepath):
    print("檔案存在。")
  
else:
    print("檔案不存在。")
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["學年", "性質", '課名', "學分", '成績', '排名'])
