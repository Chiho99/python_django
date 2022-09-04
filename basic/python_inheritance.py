class Member:
    name = 'no name'
    age = 0
    mail = 'no address'

    def __init__(self, name='noname', age=0, mail='no address'):
        self.name = name
        self.age = age
        self.mail = mail

    def print(self):
        print(self.name + '(' + str(self.age) + ' years old. ' + self.mail+')')


class Employee(Member):
    company = 'unemployed'

    def __init__(self, company='', name='no name', age=0,  mail='no address'):
        self.company = company
        super().__init__(name, age, mail)

    def print(self):
        print(self.name + '[' + str(self.age) + self.company+']')


taro = Member('Taro Yamada', 39, 'sample@sample.com')
taro.print()
hanako = Employee(name='Hanako Tanaka', company='Python Systems')
hanako.print()
