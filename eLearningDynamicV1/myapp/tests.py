class Dog():
    name: str
    def __init__(self, name):
        self.name = name
        print(f"僕の名前は{self.name}!!")

taro = Dog("太郎")