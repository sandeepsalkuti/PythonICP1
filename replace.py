#Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex

inp=input("enter a sentence")
if("python" in inp):
    x=inp.replace("python","pythons")  #applied replace method to input string and replaced string
    print(x)
else:
    print("use python in sentence") # as question says to replace with python upon not existing asking to use it in sentence