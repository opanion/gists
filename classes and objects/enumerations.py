from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 3
    ORANGE = 2
    MELON = 4
    PEAR = auto()




print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))

print(Fruit.PEAR.name, Fruit.PEAR.value)



