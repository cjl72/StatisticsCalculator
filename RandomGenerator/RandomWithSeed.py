from numpy.random import seed
from numpy.random import uniform
from numpy.random import randint

class RandomWithSeed():
    @staticmethod
    def randomInt(sd, a, b):
        seed(sd)
        num = randint(a, b)
        if isinstance(a, float):
            return RandomWithSeed.randomDec(sd, a, b)

        return num

    @staticmethod
    def randomDec(sd, a, b):
        seed(sd)
        num = uniform(a, b)

        return num