import random

#a
number = int(input("Enter a non negative number? "))
num = 1

if number == 0:
    num = 1
else:
    for i in range(1,number+1):
        num*=i
print(num)

#b
print("give me 2 positive integer i give you prime numbers between them")
a = int(input("number 1 "))
b = int(input("number 2 "))

min = a
max = b
if b<a:
    min = b
    max = a

for i in range(min,max+1):
    is_prime = True
    for j in range(2,i):
        if i % j == 0 :
            is_prime = False
    if is_prime and i !=1 and i != 0:
        print(i)

#3

#4
to_guess = random.randint(1,20)
while True:
    

    guess = int(input("What is your guess? "))

    if guess == to_guess:
        print("You guessed it right!")
        break
    else:
        pass
