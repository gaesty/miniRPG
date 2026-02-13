from ..InventoryStrategy import InventoryStrategy


class UseItemStrategy(InventoryStrategy):
    def execute_action(self, inventory, item):
        if "items" not in inventory or not inventory["items"]:
            print("Inventory is empty!")
            return False

        item_name = item.get("name", item) if isinstance(item, dict) else item

        for inv_item in inventory["items"]:
            if inv_item.get("name") == item_name:
                print(f"Using item '{item_name}'!")
                pv_restore = inv_item.get("pv_restore", inv_item.get("value", 0))
                damage = inv_item.get("damage", 0)
                status = inv_item.get("status", None)
                if pv_restore:
                    print(f"Effect: heal (+{pv_restore} HP)")
                elif damage:
                    print(f"Effect: damage ({damage})")
                elif status:
                    print(f"Effect: {status}")
                else:
                    print("Effect: No effect")
                inventory["items"].remove(inv_item)
                return inv_item

        print(f"Item '{item_name}' not found in inventory!")
        return False

    def get_strategy_name(self):
        return "Use Item"
