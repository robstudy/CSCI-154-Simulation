# Assignment 1
# Part 3
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019


class Hamburger:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self, sep=''):
        return (', '.join(list(self.__dict__.values())))


burger1 = Hamburger(meat="chicken", extra1="cheese", extra2="ketchup")

print(burger1)
