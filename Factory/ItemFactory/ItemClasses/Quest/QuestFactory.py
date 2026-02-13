from KeyClass import KeyClass

class QuestFactory:
    def createQuestItem(self, name):
        if name == "key":
            return KeyClass()
        else:
            pass
