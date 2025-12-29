'''def greed(name):
    print(f"Привет, {name}!")
greed(input())'''

'''def square(number):
    print(int(number)*int(number))
square(int(input()))'''

'''x=int(input())
y=int(input())
def max_of_two(x,y):
    if x>y:
        print(x)
    if y>x:
        print(y)
    else:
        print(x)
max_of_two(x,y)'''#1

'''def describe_person(name,age=30):
    print(f"Имя {name}")  
    print(f"Возраст: {age}") 

describe_person("Добрыня")'''#2

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
            
    return True
print(is_prime(int(input())))#3

