# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
import string
class Alphabet:
    def __init__(self,leng,letters):
        self.leng=leng
        self.letters=letters
    def prin(self):
        return self.letters
    def letters_num(self,letters):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num=26
    def __init__(self,leng,letters): #Инициализатор дочернего класса
        super().__init__(leng,letters)#Инициализатор родительского класса
        self.leng = 'En'
        self.letters=letters

    def is_en_letter(self,bukva):
        if bukva in self.letters:
            print(f'Буква {bukva} принадлежит английскому алфавита ')
        else:
            print(f'Буква {bukva} не принадлежит английскому алфавита ')
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        Text = 'Every day in elementary school in America begins at 9.20 a.m. Children have classes till 3.15 p.m. At 12 o’clock children have lunch. Many boys and girls bring their lunch from home. But some of them go for lunch to a school cafeteria.'
        print(Text)
    def vivod(self):
        print(self.leng, self.letters)

letters=string.ascii_uppercase
English=EngAlphabet('En',letters)
English.vivod()
print('Буквы английского алфавита  ', English.letters) #Буквы алфавита
print('Количество букв в алфавите ',English.letters_num())
English.is_en_letter('F')
English.is_en_letter('Щ')
print('Пример текста на английском языке   ')
English.example()





