import random 

print("Welcome to the Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*.?0123456789"

amount_password=input("Enter the amount of passwords you want to generate: ")
amount_password=int(amount_password)

length_password=input("Enter the length of the password: ")
length_password=int(length_password)

for i in range(amount_password):
    password="".join(random.sample(chars,length_password))
    print(password)