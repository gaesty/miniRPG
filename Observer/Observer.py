class FinalBoss:
    def __init__(self):
        pass
        
    is_awake = False

    def update(self):
        print(f"Final Boss is ready !\n")

class DungeonEvent:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def enemy_defeated(self, dungeon):
        for observer in self.observers:
            if observer == 1:
                observer.update(dungeon)
                boss = FinalBoss()
                boss.is_awake = True
            else:
                return "Final boss is not ready to fight"
