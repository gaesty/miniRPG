class QuestState:
    def start(self, quest):
        pass
    
    def complete(self, quest):
        pass
    
    def fail(self, quest):
        pass
    
    def get_status(self):
        pass


class NotStarted(QuestState):
    def start(self, quest):
        print(f"Quest '{quest.name}' has started!")
        quest.state = InProgress()
    
    def complete(self, quest):
        print(f"Quest '{quest.name}' cannot be completed. It has not started yet.")
    
    def fail(self, quest):
        print(f"Quest '{quest.name}' cannot fail. It has not started yet.")
    
    def get_status(self):
        return "Not Started"


class InProgress(QuestState):
    def start(self, quest):
        print(f"Quest '{quest.name}' is already in progress.")
    
    def complete(self, quest):
        print(f"Quest '{quest.name}' completed!")
        quest.state = Completed()
    
    def fail(self, quest):
        print(f"Quest '{quest.name}' has failed.")
        quest.state = Failed()
    
    def get_status(self):
        return "In Progress"


class Completed(QuestState):
    def start(self, quest):
        print(f"Quest '{quest.name}' is already completed.")
    
    def complete(self, quest):
        print(f"Quest '{quest.name}' is already completed.")
    
    def fail(self, quest):
        print(f"Quest '{quest.name}' is already completed and cannot fail.")
    
    def get_status(self):
        return "Completed"


class Failed(QuestState):
    def start(self, quest):
        print(f"Quest '{quest.name}' has failed and cannot be restarted.")
    
    def complete(self, quest):
        print(f"Quest '{quest.name}' has failed and cannot be completed.")
    
    def fail(self, quest):
        print(f"Quest '{quest.name}' has already failed.")
    
    def get_status(self):
        return "Failed"


class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward
        self.state = NotStarted()
    
    def start(self):
        self.state.start(self)
    
    def complete(self):
        self.state.complete(self)
    
    def fail(self):
        self.state.fail(self)
    
    def get_status(self):
        return self.state.get_status()
    
    def get_info(self):
        return {
            "name": self.name,
            "description": self.description,
            "reward": self.reward,
            "status": self.get_status()
        }
