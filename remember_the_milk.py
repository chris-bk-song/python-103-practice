count = 0
groceries = ''
while count < 3:
    groceries = groceries + input ('What do you need from the store today? ')
    groceries = groceries + '\n' # Add a line break after each grocery item
    count = count + 1
print(f'Here is your grocery list:\n{groceries}')