lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name,
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

# print(player.name)
# print(player.total())

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    # @staticmethod and @classmethod are decorators
    # static method passes no parameters
    # class method passes the class as the first parameter
    # normal methods pass self as the first parameter
    def go_to_school():
        print("I'm going to school.")

anna = Student('Anna', 'MIT')
rolf = Student('Rolf', 'Oxford')

anna.marks.append(56)
anna.marks.append(77)
anna.marks.append(86)
print(anna.average())
Student.go_to_school()