class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == "age":
            self.__dict__[attr] = value + 10 # Не self.имя = значение или setattr
        else:
            raise AttributeError(attr + " not allowed") # Не разрешено

X = Accesscontrol()
X.age = 60
print(X.age)
X.name = "Bob"

# self.__dict__[attr] = value + 10 # Нормально: Зацикливания нет
# object.__setattr__(self, attr, key, value + 10) # Нормально: Зацикливания нет