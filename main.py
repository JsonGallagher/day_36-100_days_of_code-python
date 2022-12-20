names = []

def printNames():
  print()
  print("Name List:")
  for name in names:
    print(name)
  print()

while True:
  first_name = input("What is your first name? ").strip().capitalize()
  last_name = input("What is your last name? ").strip().capitalize()
  full_name = f"{first_name} {last_name}"
  if full_name not in names:
    names.append(full_name)
  else:
    print("That name is already in the list.")
  printNames()