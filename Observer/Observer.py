class FinalBoss:
    def __init__(self):
        self.is_awake = False

    def update(self, enemies_defeated):
        self.is_awake = True
        print(f"Final Boss is ready! ({enemies_defeated} enemies defeated)\n")


class DungeonEvent:
    def __init__(self):
        self.observers = []
        self.threshold = 1

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def enemy_defeated(self, enemies_defeated):
        if enemies_defeated >= self.threshold:
            for observer in self.observers:
                observer.update(enemies_defeated)
        else:
            print("Final boss is not ready to fight")
