title = "\033[34mTo Do List Manager\033[0m" 
print(f"{title:^60}")
print()
print ("\033[36mManage your to-do list: view, add or edit\033[0m")

import os, time
toDoList = []

def view():
  print() 
  for item in toDoList:
    print(f"{item:<30}")
  print() 

while True:
  print()
  menu = input("What would you like to do? ")
  print()
  if menu == "add":
    item = input("Who should I add to the to do list?: ")
    toDoList.append(item)

  elif menu == "edit":
    item = input("Who should I remove from the to do list?:  ")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} was not in the list")

  elif menu == "view":
    print()
    print("Here is your to do list: ")

  view() 
  time.sleep(2)
  os.system("clear")
  print(f"{title:^60}")