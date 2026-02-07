#!/usr/bin/env python3
"""
Test script for the Console Todo App
"""

from src.services.todo_service import TodoService
from src.repository.todo_repository import TodoRepository


def test_todo_app():
    # Create a service with a fresh repository
    service = TodoService(TodoRepository())

    print("Testing Todo App functionality...\n")

    # Test adding tasks
    print("1. Adding tasks:")
    id1 = service.add_task("Buy groceries")
    print(f"   Added task with ID: {id1}")

    id2 = service.add_task("Finish report")
    print(f"   Added task with ID: {id2}")

    # Test listing tasks
    print("\n2. Listing all tasks:")
    tasks = service.get_all_tasks()
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        print(f"   ID: {task['id']}, Status: {status}, Title: {task['title']}")

    # Test updating a task
    print("\n3. Updating task:")
    success = service.update_task(id1, "Buy weekly groceries")
    print(f"   Update successful: {success}")

    # List tasks again to see the update
    print("\n4. Listing tasks after update:")
    tasks = service.get_all_tasks()
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        print(f"   ID: {task['id']}, Status: {status}, Title: {task['title']}")

    # Test marking a task as complete
    print("\n5. Marking task as complete:")
    success = service.toggle_task_completion(id1)
    print(f"   Toggle completion successful: {success}")

    # List tasks again to see the completion status
    print("\n6. Listing tasks after marking complete:")
    tasks = service.get_all_tasks()
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        print(f"   ID: {task['id']}, Status: {status}, Title: {task['title']}")

    # Test deleting a task
    print(f"\n7. Deleting task with ID {id2}:")
    success = service.delete_task(id2)
    print(f"   Deletion successful: {success}")

    # List tasks again to see the deletion
    print("\n8. Listing tasks after deletion:")
    tasks = service.get_all_tasks()
    if tasks:
        for task in tasks:
            status = "[x]" if task['completed'] else "[ ]"
            print(f"   ID: {task['id']}, Status: {status}, Title: {task['title']}")
    else:
        print("   No tasks in your todo list.")

    print("\nTest completed successfully!")


if __name__ == "__main__":
    test_todo_app()