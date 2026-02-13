from AxeClass import AxeClass
from BowClass import BowClass
from KnifeClass import KnifeClass
from MagicStickClass import MagicStickClass
from SteelSwordClass import SteelSwordClass
from WoodenSwordClass import WoodenSwordClass


class WeaponFactory:
    def createWeapon(self, name):
        if name == "woodensword":
            return WoodenSwordClass()
        elif name == "steelsword":
            return SteelSwordClass()
        elif name == "magicstick":
            return MagicStickClass()
        elif name == "knife":
            return KnifeClass()
        elif name == "axe":
            return AxeClass()
        elif name == "bow":
            return BowClass()
        else:
            pass
