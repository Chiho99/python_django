class Member:
    name = 'no name'
    age = 0
    mail = 'no address'

    def print(self):
        print(self.name + '(' + str(self.age) + ' years old. ' + self.mail + ')')


# インスタンス作成
taro = Member()

# 変数に値を設定
taro.name = 'Taro Yamada'
taro.age = 39
taro.mail = 'sample@sample.com'

# メソッドを実行する
taro.print()
