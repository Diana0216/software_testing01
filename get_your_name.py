# Version_1

class UserData():
    def __init__(self):
        self.name = raw_input("name:  ")
        self.numbers = []


    def my_name(self):
        return self.name


    def average(self):
        i = input("Please, enter yours numbers:  ")
        self.numbers.append(i)
        return float(sum(i)) / len(i)


res = UserData()
print res.my_name()
print res.average()


# Version_2
class UserData():
    def __init__(self):
        self.name = 'Diana'
        self.elements = []


    def my_name(self):
        return self.name


    def average(self):
        return sum(self.elements) / len(self.elements)


user = UserData()
print user.my_name()
user.elements.append(24)
user.elements.append(18)
user.elements.append(9)
print user.average()

