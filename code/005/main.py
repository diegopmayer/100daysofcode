#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nrl_count, nrs_count, nrn_count = 0, 0, 0
password = str()
for chose in range(0, nr_letters+nr_symbols+nr_numbers+1):
    if nrl_count < nr_letters:
        nrl_count += 1
        password += random.choice(letters)
    if nrs_count < nr_symbols:
        nrs_count += 1
        password += random.choice(symbols)
    if nrn_count < nr_numbers:
        nrn_count += 1
        password += random.choice(numbers)
print(password)