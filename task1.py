import json
import os

class ToDoItem:
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        item = ToDoItem(data["id"], data["title"], data["description"])
        item.completed = data["completed"]
        return item

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.id}: {self.title} - {self.description} [{status}]"


class ToDoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.items = []
        self.next_id = 1
        self.load_items()

    def add_item(self, title, description=""):
        item = ToDoItem(self.next_id, title, description)
        self.items.append(item)
        self.next_id += 1
        print(f"Added: {item}")
        self.save_items()

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]
        print(f"Removed item with ID {item_id}")
        self.save_items()

    def mark_complete(self, item_id):
        for item in self.items:
            if item.id == item_id:
                item.mark_complete()
                print(f"Completed: {item}")
                break
        self.save_items()

    def list_items(self):
        if not self.items:
            print("No items in the to-do list.")
        for item in self.items:
            print(item)

    def save_items(self):
        with open(self.filename, 'w') as file:
            json.dump([item.to_dict() for item in self.items], file, indent=4)

    def load_items(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                items = json.load(file)
                self.items = [ToDoItem.from_dict(item) for item in items]
                if self.items:
                    self.next_id = max(item.id for item in self.items) + 1


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add item")
        print("2. Remove item")
        print("3. Mark item as complete")
        print("4. List items")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the title: ")
            description = input("Enter the description (optional): ")
            todo_list.add_item(title, description)
        elif choice == "2":
            item_id = int(input("Enter the ID of the item to remove: "))
            todo_list.remove_item(item_id)
        elif choice == "3":
            item_id = int(input("Enter the ID of the item to mark as complete: "))
            todo_list.mark_complete(item_id)
        elif choice == "4":
            todo_list.list_items()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


main()

