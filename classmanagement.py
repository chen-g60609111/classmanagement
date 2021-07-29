import csv
run = 1
while(run == 1):
    print("1:已修課程; 2:未修課程; 3:輸入資料; 4:計算學分; 5:結束")
    mode = input("請輸入模式:")
    if(mode == "1"):
        print("已修課程")
    elif(mode == "2"):
        print("未修課程")
    elif(mode == "3"):
        print("輸入資料")
        with open('output.csv', 'a', newline='') as csvfile:
    elif(mode == "4"):
        print("計算學分")
    elif(mode == "5"):
        print("結束")
        break
    else:
        continue
