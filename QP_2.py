# Ex.2 Implement a Python program that simulates a real-world system or process using conditions and iterative loops
#     a.check whether an alphabet is a vowel or consonant, 
#     b. the sum of all even numbers from 0 to n, 
#     c. factorial of a number

# a. check whether an alphabet is a vowel or consonant

a=input("Enter an alphabet: ")
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("It is a vowel")
else:
    print("It is a consonant")

# b. the sum of all even numbers from 0 to n

n=int(input("Enter a number: "))
sum=0
for i in range(0, n+1, 2):
    sum+=i
print("The sum of all even numbers ", n, "is", sum)

# c. factorial of a number

n=int(input("Enter a number: "))
fact=1
for i in range(1, n+1):
    fact*=i
print("The factorial of", n, "is", fact)

