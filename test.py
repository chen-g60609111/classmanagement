#this is a modal
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
print(type(class1.turnlist()))
print(class1.name)

