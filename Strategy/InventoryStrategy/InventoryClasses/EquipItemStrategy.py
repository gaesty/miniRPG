from ..InventoryStrategy import InventoryStrategy

class EquipItemStrategy(InventoryStrategy):
    def execute_action(self, inventory, item):
        if "items" not in inventory or not inventory["items"]:
            print("Inventory is empty!")
            return False
        
        if "equipped" not in inventory:
            inventory["equipped"] = {}
        
        item_name = item.get('name', item) if isinstance(item, dict) else item
        
        for inv_item in inventory["items"]:
            if inv_item.get('name') == item_name:
                item_type = inv_item.get('type', 'misc')
                
                if item_type in inventory["equipped"]:
                    old_item = inventory["equipped"][item_type]
                    inventory["items"].append(old_item)
                    print(f"Unequipped '{old_item.get('name')}' from {item_type} slot")
                
                inventory["equipped"][item_type] = inv_item
                inventory["items"].remove(inv_item)
                print(f"Equipped '{item_name}' to {item_type} slot!")
                return True
        
        print(f"Item '{item_name}' not found in inventory!")
        return False
    
    def get_strategy_name(self):
        return "Equip Item"
