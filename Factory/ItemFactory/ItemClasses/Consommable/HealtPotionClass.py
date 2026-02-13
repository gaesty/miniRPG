class HealtPotionClass:
    def createConsommable(self, name):
        return {
            "name" : name,
            "pv_restore" : 30,
            "damage" : None,
            "status" : None
        }