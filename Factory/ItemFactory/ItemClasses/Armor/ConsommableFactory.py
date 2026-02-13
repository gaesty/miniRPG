from CapeClass import CapeClass
from LeatherArmorClass import LeatherArmorClass
from MisticDressClass import MisticDressClass
from SteelArmorClass import SteelArmorClass


class ArmorFactory:
    def createArmor(self, name):
        if name == "leatherarmor":
            return LeatherArmorClass()
        elif name == "steelarmor":
            return SteelArmorClass()
        elif name == "misticdress":
            return MisticDressClass()
        elif name == "cape":
            return CapeClass()
        else:
            pass
