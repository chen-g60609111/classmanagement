import csv

class ClassData:
    def __init__(self,semester, kind, name,credit ,score ,rank):
        self.semester = semester
        self.kind = kind
        self.name = name
        self.credit = credit
        self.score = score
        self.rank = rank
    def turnlist(self):
        datalist = [self.semester,self.kind,self.name,self.credit,self.score,self.rank]
        return datalist
class1 = ClassData("109-1","通識","哈哈",3,"A+","5%")

run = 1
while(run == 1):
    print("1:已修課程; 2:未修課程; 3:輸入資料; 4:計算學分; 5:結束")
    mode = input("請輸入模式:")
    while(mode == "1"):
        print("已修課程")
        mode = "0"
        
    while(mode == "2"):
        print("未修課程")
        mode = "0"
    while(mode == "3"):
        print("輸入資料")
        print("學年 性質 課名 學分 成績 排名:")
        #data = input().split(" ")
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["學年", "性質", '課名', "學分", '成績', '排名'])
            writer.writerow(class1.turnlist())
        #print(data)
        mode = "0"
    while(mode == "4"):
        print("計算學分")
        
        mode = "0"
    while(mode == "5"):
        print("結束")
        run = 0
        break
