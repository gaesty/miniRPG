from InventoryStrategy.InventoryStrategy import InventoryStrategy

class RemoveItemStrategy(InventoryStrategy):
    def execute_action(self, inventory, item):
        if "items" not in inventory or not inventory["items"]:
            print("Inventory is empty!")
            return False
        
        item_name = item.get('name', item) if isinstance(item, dict) else item
        
        for inv_item in inventory["items"]:
            if inv_item.get('name') == item_name:
                inventory["items"].remove(inv_item)
                print(f"Item '{item_name}' removed from inventory!")
                return True
        
        print(f"Item '{item_name}' not found in inventory!")
        return False
    
    def get_strategy_name(self):
        return "Remove Item"
