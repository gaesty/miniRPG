class InventoryContext:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
        print(f"Strategy changed to: {strategy.get_strategy_name()}")
    
    def execute_action(self, inventory, item):
        return self.strategy.execute_action(inventory, item)
