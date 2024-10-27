#static and class method

class person(object):

    avgAge=50;

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def welcomeMsg(self):
        print("hello", self.name, "you are", self.age ,"years old" )

    @classmethod
    def clsMethodChk(cls):
        print(cls.avgAge)
    @staticmethod
    def staticMethdChk(age):
        if (age>30):
          print ("Budha")


prsn=person("Sree",56)

prsn.welcomeMsg()

person.staticMethdChk(45)

prsn.clsMethodChk()