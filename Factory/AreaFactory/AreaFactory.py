from AreaClasses.AreaDungeon import AreaDungeon
from AreaClasses.AreaForest import AreaForest
from AreaClasses.AreaVillage import AreaVillage

class AreaFactory:
    def createArea(self, name):
        if name == "forest":
            return AreaForest()
        elif name == "village":
            return AreaVillage()
        elif name == "dungeon":
            return AreaDungeon()
        else:
            pass
