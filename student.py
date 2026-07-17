class Student:
    def __init__(self,roll,name,college):
        self.roll=roll
        self.name=name
        self.college=college
    
    def display(self):
        print("="*20)
        print("Roll No : ",self.roll)
        print("Name : ",self.name)
        print("College : ",self.college)
        print("="*20)