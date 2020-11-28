import  yaml
class Animal:
    name = "defalut"
    color = "blue"
    age = 0
    gender = "男"

    def __init__(self,name,color,age,gender):
        self.name=name
        self.color=color
        self.age=age
        self.gender=gender

    def Calling(self):
        print(f"{self.name} is calling")
    def Run(self):
        print(f"{self.name} is running")

class Cat(Animal):
    def __init__(self,name,color,age,gender,hari):
        self.hair = hari
        super().__init__(name,color,age,gender)

    def skill(self):
        print(f"抓到了老鼠")

    def Calling(self):
        print(f"{self.name}在喵喵叫")

    def Total(self):
        print(f"这只猫的姓名是{self.name},颜色是{self.color},年龄是{self.age},"
              f"性别是{self.gender},毛发是{self.hair},",end="")
        self.skill()

class Dog(Animal):
    def __init__(self,name,color,age,gender):
        super().__init__(name,color,age,gender)
    def Total(self):
        print(f"这条狗名字是{self.name},颜色是{self.color},年龄是{self.age},"
              f"性别是{self.gender},毛发是{self.hair}")
    def kanjai(self):
        print("狗狗会看家，是一条忠实的好狗！")
    def Calling(self):
        print(f"{self.name}在汪汪叫")

if __name__ == '__main__':
    with open("../../yamldemo/AnimalsDemo.yml",encoding="UTF-8") as f:
        animals=yaml.safe_load(f)
    cat1 = animals['cat']
    cat = Cat(cat1['name'],cat1['color'],cat1['age'],cat1['gender'],cat1['hair'])
    cat.skill()
    cat.Total()
    cat.Calling()

    dog1= animals['dog']
    dog =Dog(dog1["name"],dog1["color"],dog1["age"],dog1["gender"])
    dog.hair = "长毛"
    dog.kanjai()
    dog.Total()




