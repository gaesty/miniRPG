from HealtPotionClass import HealtPotionClass
from AntidoteClass import AntidoteClass
from BombClass import BombClass


class ConsommableFactory:
    def createConsommable(self, name):
        if name == "healtpotion":
            return HealtPotionClass()
        elif name == "antidote":
            return AntidoteClass()
        elif name == "bomb":
            return BombClass()
        else:
            pass
