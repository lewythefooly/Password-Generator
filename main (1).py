#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if nr_letters == 0 and nr_symbols == 0 and nr_numbers == 0:
  print('Invalid entry. Password cannot have 0 characters.')
else:
  password_list = []

  letter_counter = 0
  alpha = len(letters)
  for letter in letters:
    if letter_counter < nr_letters:
      random_int = random.randint(0, alpha - 1)
      password_list.append(letters[random_int])
      letter_counter += 1

  symbol_counter = 0
  total_symbols = len(symbols)
  for symbol in symbols:
    if symbol_counter < nr_symbols:
      random_int = random.randint(0, total_symbols - 1)
      password_list.append(symbols[random_int])
      symbol_counter += 1
  
  num_counter = 0
  numerical = len(numbers)
  for num in numbers:
    if num_counter < nr_numbers:
      random_int = random.randint(0, numerical - 1)
      password_list.append(numbers[random_int])
      num_counter += 1

  password = ""
  for char in password_list:
    password += char
print(f'Simpler, but still secure password suggestion: {password}')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
if nr_letters == 0 and nr_symbols == 0 and nr_numbers == 0:
  print('Invalid entry. Password cannot have 0 characters.')
else:
  password_list = []

  letter_counter = 0
  alpha = len(letters)
  for letter in letters:
    if letter_counter < nr_letters:
      random_int = random.randint(0, alpha - 1)
      password_list.append(letters[random_int])
      letter_counter += 1

  symbol_counter = 0
  total_symbols = len(symbols)
  for symbol in symbols:
    if symbol_counter < nr_symbols:
      random_int = random.randint(0, total_symbols - 1)
      password_list.append(symbols[random_int])
      symbol_counter += 1
  
  num_counter = 0
  numerical = len(numbers)
  for num in numbers:
    if num_counter < nr_numbers:
      random_int = random.randint(0, numerical - 1)
      password_list.append(numbers[random_int])
      num_counter += 1

  random.shuffle(password_list)
  password = ""
  for char in password_list:
    password += char
print(f'Tougher to crack password suggestion: {password}')