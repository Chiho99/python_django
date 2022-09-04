class Member:
    name: 'no nanme'
    age = 0
    mail = 'no address'

    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

    def print(self):
        # 変数やメソッドはself内から呼び出す
        print(self.name + '(' + str(self.age) + ' years old. ' + self.mail + ')')


taro = Member('Taro-Yamada', 39, 'sample@sample.com')
taro.print()
hanako = Member('Hanako-Tanaka', 28, 'sample1@sample.com')
hanako.print()
