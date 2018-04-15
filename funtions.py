#using funtion

#the format for python dunction is ..
#def <name>(<input>...):
def sum1(a, b):
    c = a+b
    print(a,'+',b, '=', c)


#a funtion that return sum
def sum2(a, b):
    c = a + b
    return c

sum1(200, 3)
a = sum2(34, 21)
print('The sum I got from a return function is', a)