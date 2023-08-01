# from functions import get_todos, write_todos
# other method
import functions as fn
import time


text = """
Priciples of productivity:
Manage your inflow.
Systemizing everything that repeats
"""
print(text)
# dir(str)  - all the methods we can apply to a string data type
# import builtins
# __setitem__ can be used for item indexing, __gettime__ how to get
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:] # <- list slicing removers the add_

            todos = fn.get_todos()

            todos.append(todo + '\n')

            fn.write_todos(todos)

            # file.write('this is to write a text and not a list')
            # file.read('writes a string')
    elif user_action.startswith('show'):

            todos = fn.get_todos()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # new_todos = [item.strip('\n') for item in todos]

            print(todos)

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

    elif user_action.startswith('edit'):
        try:
                number = int(user_action[5:])
                print(number)
                number = number - 1

                todos = fn.get_todos()

                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo + '\n'

                fn.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = fn.get_todos()

            index = number - 1
            removed_todo =  todos[index].strip('\n')
            todos.pop(index)

            fn.write_todos(todos)

            message= f"Todo {removed_todo} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
            break

    else:
        print("You've entered an unknown command!")
        # case _:
        #     print("You've entered an unknown command!")

print("Bye!")