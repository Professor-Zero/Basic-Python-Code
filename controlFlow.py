#if statements, while loops, and for loops
#python doesn't not use curly brases to start and end a if statment, for loops, and whileloops this is used ':'

string = "ahdkhashahf8*asd ashidiaf@"

print("if statments-------------------------")
#python has a in option to check is something is in a string.
#instead of doing string.contains("8") in java.
if '8' in string:
    index = string.find('8')
    print("your string has 8 at index", index)
#python uses elif instead of else if like in java or c++
#not option is like the ! when used in java or c++.
elif '' not in string:
    print("8 is not in string")

if '*' in string:
    index = string.find('*')
    print("your string has * at index", index)

if '@' in string:
    index = string.find('@')
    print("your string has @ at index", index)
print("--------------------------------------")

print("for loops-----------------------------")

string = 'Today'
#for loops statments is different uses
#for <name variable that will be used by for loop> in <get length/use a string>
#range() must be used to tell the for loop how many time you want it to run.
for i in range(len(string)):
    print('index:', i, 'character:', string[i])
print("--------------------------------------")

print("while loop-----------------------------")

string = '******************'
count = 1
while len(string) != 0:
    print(string)
    string = string[0:len(string)-count]
    #can't use count++ to increment in python.
    count += 1
print('end of while loop')
print("--------------------------------------")