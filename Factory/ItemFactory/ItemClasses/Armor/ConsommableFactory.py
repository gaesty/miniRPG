from CapeClass import CapeClass
from LeatherArmorClass import LeatherArmorClass
from MisticDressClass import MisticDressClass


class ArmorFactory:
    def createArmor(self, name):
        if name == "leatherarmor":
            return LeatherArmorClass()
        elif name == "misticdress":
            return MisticDressClass()
        elif name == "cape":
            return CapeClass()
        else:
            pass
