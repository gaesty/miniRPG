class BombClass:
    def createConsommable(self, name):
        return {
            "name" : name,
            "pv_restore" : None,
            "damage" : 30,
            "status" : None
        }