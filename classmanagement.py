#C:\Users\111\Desktop\31634\python_file\env_classmanagement\Scripts
import csv
import os

filepath = "./output.csv"
if os.path.isfile(filepath):
    print("檔案存在。")
else:
    print("檔案不存在。建立")
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["學年", "性質", '課名', "學分", '成績', '排名'])

class ClassData:
    def __init__(self,semester, kind, name,credit ,score ,rank):
        self.semester = semester   #學期
        self.kind = kind           #課程分類
        self.name = name           #課名
        self.credit = credit       #學分
        self.score = score         #分數
        self.rank = rank           #排名
    def __str__(self):
        return self.name
        
    def turnlist(self):
        datalist = [self.semester,self.kind,self.name,self.credit,self.score,self.rank]
        return datalist
    
    def printdata(self,lens):
        #print(self.semester, self.kind, "  "*(lens-len(self.name))+self.name,self.credit,self.score,self.rank)
        print("%3s %2s" %(self.semester,self.kind), end = " ")
        print("  "*(lens-len(self.name))+self.name, end = " ")
        print("%4s %4s %4s" %(self.credit,self.score,self.rank))
    
class1 = ClassData("109-1","通識","哈哈",3,"A+","5%")

def sortclass(classlist):
    new_classlist = [[] for i in range(24)]
    semesterindex = ["108-1","108-2","109-1","109-2","110-1","110-2","111-1","111-2"]
    for myclass in classlist:
        index = semesterindex.index(myclass.semester)
        if myclass.kind == "必修":
            new_classlist[index*3+0].append(myclass)
        elif myclass.kind == "選修":
            new_classlist[index*3+1].append(myclass)
        elif myclass.kind == "通識":
            new_classlist[index*3+2].append(myclass)
    result = []           
    for i in range(24):
        new_classlist[i] = sorted(new_classlist[i], key = lambda s: len(s.name))
        result.extend(new_classlist[i])
    # for i in range(24):
        # for j in new_classlist[i]:
            # print(j, end = " ")
        # print()
    return result

run = 1
while(run == 1):
    print("1:已修課程; 2:檢視學分; 3:輸入資料; 4:修改; 5:結束")
    mode = input("請輸入模式:")
    lens = 0
    with open('output.csv', newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = list(csv.reader(csvfile))
        classlist = []
        for row in range(1,len(rows)):
            theclass = ClassData(rows[row][0],rows[row][1],rows[row][2],rows[row][3],rows[row][4],rows[row][5])
            classlist.append(theclass)
            if len(rows[row][2]) > lens:
                lens = len(rows[row][2])
    classlist = sortclass(classlist)

    # mode = "1"

    while(mode == "1"):
        print("已修課程")
        print("%3s %2s" %(rows[0][0],rows[0][1]), end = " ")
        print("  "*(lens-len(rows[0][2]))+rows[0][2], end = " ")
        print("%s %s %s" %(rows[0][3],rows[0][4],rows[0][5]))
        print("----------------------------------------")
        for i in range(len(classlist)):
            classlist[i].printdata(lens)
        print()
        mode = "0"

        
    while(mode == "2"):
        print("檢視學分")
        print("必修: 20/30   選修: 15/60   通識: 5/16")
        print("----------------------------------------")
        list1 = []
        list2 = []
        list3 = []
        for i in range(len(classlist)):
            if classlist[i].kind == "必修":
                list1.append(classlist[i])
            elif classlist[i].kind == "選修":
                list2.append(classlist[i])
            elif classlist[i].kind == "通識":
                list3.append(classlist[i])
        list1 = sorted(list1, key = lambda s: (s.name))
        list2 = sorted(list2, key = lambda s: (s.name))
        list3 = sorted(list3, key = lambda s: (s.name))
        print("必修：")
        for i in list1:
            print(i.name,i.credit)
        print()    
        print("選修：")
        for i in list2:
            print(i.name,i.credit)
        print()
        print("通識：")
        for i in list3:
            print(i.name,i.credit)
        print()
        mode = "0"
        
    while(mode == "3"):
        print("輸入資料")
        print("學年 性質 課名 學分 成績 排名:")
        t = ["學年", "性質", "課名", "學分", "成績", "排名"]
        data = input().split(" ")
        if data[0] == "":
            mode = "0"
            break        
        if len(data) != 6:
            print("輸入錯誤")            
            print()
            continue       
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
        print()
        
    while(mode == "4"):
        print("修改")
        print("編號", end = " ")
        print("%3s %2s" %(rows[0][0],rows[0][1]), end = " ")
        print("  "*(lens-len(rows[0][2]))+rows[0][2], end = " ")
        print("%s %s %s" %(rows[0][3],rows[0][4],rows[0][5]))
        print("----------------------------------------")
        for i in range(len(classlist)):
            print("%4d" %(i+1), end = " ")
            classlist[i].printdata(lens)
        target = input("修改項目:")
        if target == "" or type(target)!="int":
            mode = "0"
            break
        elif int(target) <= len(classlist):
            target = int(target)
        else:
            print("無此項目")
            print()
            continue
        print("修改前:",end = "")
        print(classlist[target-1].semester,classlist[target-1].kind,classlist[target-1].name,classlist[target-1].credit,classlist[target-1].score,classlist[target-1].rank)
        revise = input("修改後:").split(" ")
        if len(revise) != 6:
            mode = "0"
            break
        revise_class = ClassData(revise[0],revise[1],revise[2],revise[3],revise[4],revise[5])
        classlist[target-1] = revise_class
        print()
        t = ["學年", "性質", "課名", "學分", "成績", "排名"]
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(t)
            for i in classlist:
                writer.writerow(i.turnlist())

        # print("清除資料")
        # check = input("yes/no:")
        # t = ["學年", "性質", "課名", "學分", "成績", "排名"]
        # if check == "yes":
            # with open('output.csv', 'w', newline='') as csvfile:
                # writer = csv.writer(csvfile)
                # writer.writerow(t)
        
        mode = "0"
    while(mode == "5"):
        print("結束")
        run = 0
        break
