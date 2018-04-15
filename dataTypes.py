#first topic on data type

#this is a string, python automatically know the type.
#so no need to tell what type it is.
string = "Mohamed,Abdi"

print("Full name:")
print(string)
print() #gives it a new line.

#getting the first name.
firstName = string[0:7]
#getting the last name 
lastName = string[8:len(string)]
#getting th comma
comma = string[7]

print("First name:")
print(firstName)
print()
print("Last name:")
print(lastName)
print()
print("comma:")
print(comma)
print()

height = 10
width = 30

area = height * width
#you can put comma in print statement to add it to the same line
print("Height:", height, "width:",width)
print("Area:",area)