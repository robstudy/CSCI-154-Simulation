# Assignment 1
# Part 3
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019


class Hamburger:
    def __init__(self, **kwargs):
        # object attributes are mapped to the keyword arguments
        # self dictionary is used to store mappings
        self.__dict__ = kwargs

    def __str__(self, sep=''):
        return (', '.join(list(self.__dict__.values())))


# different test cases with varying amount of arguments
burger1 = Hamburger(meat="chicken", extra1="cheese", extra2="ketchup")
burger2 = Hamburger(meat="beef", extra1="cheese", extra2="mayo")
burger3 = Hamburger(meat="snake", extra1="tarter sauce", extra2="peanuts", extra3="motor oil")

print(burger1)
print(burger2)
print(burger3)
