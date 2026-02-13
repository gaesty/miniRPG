from PlayerClasses import Warrior, Mage, Thief

class PlayerFactory:
    def createEnemy(self, name):
        if name == "warrior":
            return Warrior()
        elif name == "mage":
            return Mage()
        elif name == "thief":
            return Thief()
        else:
            pass
