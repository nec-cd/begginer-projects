import random
print ("Welcome to the password generator!")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


num_letters= int(input("How many letters would you like in your password?"))
num_symbols= int(input("How many symbols would you like in your password?"))
num_numbers= int(input("How many numbers would you like in your password?"))


password= []

for char_lett in range (1, num_letters+1):
    lett=random.choice(letters)
    password.append(lett)
    
for char_sym in range (1, num_symbols+1):
    sym=random.choice(symbols)
    password.append(sym)
    
for char_num in range (1, num_numbers+1):
    num=random.choice(numbers)
    password.append(num)


random.shuffle(password)

password_print="".join(password)

print(f"Your password is: '{password_print}'")
    
    
