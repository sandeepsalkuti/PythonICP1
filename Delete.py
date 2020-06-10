#Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it

ip=input("enter string")
x=ip[1:2] + ip[2:]
y=x[1:2] + x[2:]                   # Using slice method and removing first two characters
# After deleting two characters final string is
print("string after deletion",y)
final=y[::-1]
print("string after reversal",final)











# Take two numbers from user and perform arithmetic operations on them
num1=int(input("enter first number"))
num2=int(input("enter second number"))
# performing all basic arithmetic operations
print("addition is",num1 + num2)
print("substraction is",num1-num2)
print("multiplication is",num1 * num2)
print("division is",num1 / num2)
print("modulus operation is",num1%num2)
print("exponent operation is",num1 ** num2)
print("floor division is",num1//num2)
