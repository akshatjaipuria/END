# write a python program to add two numbers 
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print(f'Sum: {sum}')


# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


# write a program to find and print the largest among three numbers

num1 = 10
num2 = 12
num3 = 14
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print(f'largest:{largest}')


# write a program to find and print the smallest among three numbers
num1 = 10
num2 = 12
num3 = 14
if (num1 <= num2) and (num1 <= num3):
   smallest = num1
elif (num2 <= num1) and (num2 <= num3):
   smallest = num2
else:
   smallest = num3
print(f'smallest:{smallest}')


# Write a python function to merge two given lists into one
def merge_lists(l1, l2):
    return l1 + l2


# Write a program to check whether a number is prime or not
num = 337

if num > 1:
   for i in range(2, num//2 + 1):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(f"{i} times {num//i} is {num}")
           break
   else:
       print(f"{num} is a prime number")

else:
   print(f"{num} is not a prime number")


# Write a python function that prints the factors of a given number
def print_factors(x):
   print(f"The factors of {x} are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# Write a program to find the factorial of a number
num = 13
factorial = 1

if num < 0:
   print("No factorials for negative numbers!")

elif num == 0:
   print("The factorial of 0 is 1")

else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(f"The factorial of {num} is {factorial}")


# Write a python function to print whether a number is negative, positive or zero
def check_pnz(num):
    if num > 0:
       print("Positive number")

    elif num == 0:
       print("Zero")

    else:
       print("Negative number")


# Write a program to print the multiplication table of a given number

num = 9
for i in range(1, 11):
   print(f"{num} x {i} = {num*i}")


# Write a python function to print powers of 2, for given number of terms
def two_power(terms):
    result = list(map(lambda x: 2 ** x, range(terms)))

    print(f"The total terms are: {terms}")
    for i in range(terms):
       print(f"2^{i} = {result[i]}")


# Write a program to filter the numbers in a list which are divisible by a given number
my_list = [11, 45, 74, 89, 132, 239, 721, 21]

num = 3
result = list(filter(lambda x: (x % num == 0), my_list))

print(f"Numbers divisible by {num} are {result}")


# Write a python function that returns the sum of n natural numbers
def sum_natural(num):
    if num < 0:
       print("Please enter a positive number!")
    else:
       sum = 0
       while(num > 0):
           sum += num
           num -= 1
       return num

# Write a program to swap first and last elements in a list
my_list = [1, 2, 3, 4, 5, 6]
my_list[0], my_list[-1] = my_list[-1], my_list[0]


# Write a python function to find the area of a circle, whose radius is given
def findArea(r): 
    PI = 3.142
    return PI * (r*r)


# Write a program to print the sum of squares of first n natural numbers
n = 21
sum_n = 0
for i in range(1, n+1):
    sum_n += i**2
print(sum_n)


# Write a program to print the length of a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(my_list))


# Write a pythno function to print the length of a given tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

print(len(my_tuple))


# Write a python function to print the elements of a given list, one element in a line
def custom_print(l):
    for _ in l:
        print(_)


# Write a python function to remove all the odd numbers from a list and return the remaining list

def remove_odd(my_list):
    result = list(filter(lambda x: (x % 2 == 0), my_list))
    return result


# Write a python function to remove all the even numbers from a list and return the remaining list

def remove_even(my_list):
    result = list(filter(lambda x: (x % 2 != 0), my_list))
    return result


# Write a function that takes two lists as input and returns a zipped list of corresponding elements

def zip_list(list1, list2):
    return list(zip(list1, list2))


# Write a program to to print the contents of a given file
file_name = 'temp.txt'
with open(file_name, 'r') as f:
    print(f.read())


# Write a functin that returns the LCM of two input numbers

def lcm(a, b):
    if a>b:
        min_ = a
    else:
        min_ = b
    while True:
        if min_%a==0 and min_%b==0:
            break
        min_+=1
    return min_


# Write a program to print the unique elements in a list
my_list = [1, 2, 4, 5, 2, 3, 1, 5, 4, 7, 8, 2, 4, 5, 2, 7, 3]

print(set(my_list))


# Write a function that returns the sum of digits of a given number
def digisum(num):
    sum_=0
    while num > 0:
        dig = num % 10
        sum_+=dig
        num//=10
    return sum_


# Write a program to check and print whether a number is palindrome or not

num = 12321
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev*10 + dig
    num//=10
if temp==rev :
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# Write a function that prints a given value, n number of times
def print_n(val, n):
    for _ in range(n):
        print(val)


# Write a function to find the area of sqaure
def square_area(a):
    return a*a


# Write a function to find the perimeter of a square
def square_perimeter(a):
    return 4*a

# Write a function to find the area of rectangle
def rectangle_area(l, b):
    return l*b

# Write a function to find the permieter of a rectangle
def rectangle_perimeter(l, b):
    return 2*(l+b)

# Write a python function to find the area of a circle, whose radius is given
def findArea(r): 
    PI = 3.142
    return PI * (r*r)

# Write a function to calculate and return electricity bill. Units used are given. Price per unit is fixed and is increased after 750 units.

def calc_elect_bill(units):
    if units > 0:
        if units <= 750:
            return 5*units
        else:
            return 5*(750) + 7*(units-750)

    else:
        return -1


# Write a function to return day of a week, given the number
def give_day(n):
    day_dict = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    return day_dict[n]


# Write a program to calculate and print the volume of a cylender
r = 3
h = 5
pi = 3.14
volume = pi*(r**2)*h
print(volume)


# Write a function to calculate and return the average of input numbers

def calc_avg(*args):
    if len(args) > 0:
        return sum(args)/len(args)
    return None


# Write a function to calculate compound interest, given p, r, t
def comp_int(p, r, t):
    amount = p * (1 + (r/100))**t
    interest = amount - p
    return interest


# Write a function to calculate simple interest, given p, r, t
def simp_int(p, r, t):
    interest = (p*r*t)/100
    return interest


# Write a program to print a given string, replacing all the vowels with '_'

st = "Where is this going? Could you please help me understand!"
vowels = "AEIOUaeiou"

for v in vowels:
    st = st.replace(v, '_')

print(st)


# Write a functio to check whether a number if perfect or not
def is_perfect(n):
    sum_ = 0
    for i in range(1, n//2 + 1):
        if n%i == 0:
            sum_+=i
    if sum_ == n:
        return True
    return False

# Write a function that returns seperate lists of positive and negative numbers from an input list
def seperate_pn(l):
    pos_list = []
    neg_list = []
    for _ in l:
        if _<0:
            neg_list.append(_)
        else:
            pos_list.append(_)
    return pos_list, neg_list


# Write a program to find and print the area of a triangle, whose hight and width are given.

h = 12
w = 11
area = 0.5*h*w
print(area)


# Write a function to find acceleration, given u, v and t

def acc(u, v, t):
    return (v-u)/t

# Write a lambda function to multiply two numbers

multiply = lambda a, b: a*b

# Write a lambda function to add two numbers

add = lambda a, b: a+b

# Write a lambda function that gives True if the input number is even otherwise False

even = lambda a: True if a%2 == 0 else False

# Write a lambda function to to give character grom it's ascii value

ascii = lambda a: chr(a)

# Write a lambda function to that gives the number of digits in a number

dig_cnt = lambda a: len(str(a))

# Write a program to to check if a triangle is valid or not, given it's all three angles

def is_valid_triangle_angle(a, b c):
    if a+b+c == 180:
        return True
    return False

# Write a program to to check if a triangle is valid or not, given it's all three sides' length

def is_valid_triangle_length(a, b c):
    if a>0 and b>0 and c>0:
        if a+b > c and a+c > b and b+c > a:
            return True
    return False

# Write a lambda functio that gives the word count in a statement.

count_word = lambda s: len(s.split(' '))


# Write a program to extract and print digits of a number in reverse order. The number is input from user.

num = int(input("Enter a number with multiple digit: "))
n=0
while num>0:
    a = num%10
    num = num - a
    num = num/10
    print(int(a),end="")
    n = n + 1

# Write a function that takes in height(m) and weight(kg), calculates BMI and prints the comments

def bmi(height: "Meters", weight: "Kgs"):
    bmi = weight/(height**2) 
    print("Your BMI is: {0} and you are ".format(bmi), end='')
    if ( bmi < 16):
       print("severely underweight.")
    elif ( bmi >= 16 and bmi < 18.5):
       print("underweight.")
    elif ( bmi >= 18.5 and bmi < 25):
       print("healthy.")
    elif ( bmi >= 25 and bmi < 30):
       print("overweight.")
    elif ( bmi >=30):
       print("severely overweight.") 

# Write a program that prints all the alphabets in a string and skips all other characters

string = "$john.snow#@Got.bad_ending/com"
for ch in string:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        print(ch, end='')
    else:
        pass

# Write a function that takes number of disks in tower of hanaoi problem and returns the minimum number of steps required

def hanoi(x):
    if x == 1:
        return 1
    else:
        return 2*hanoi(x-1) + 1

# Write a lambda function to convert centimeters to inches

cm_to_inch = lambda x: x/2.54

# Write a lambda function to find the union of two lists

union = lambda a, b: list(set(a)|set(b))

# Write a lambda function to find the intersection of two lists

intersection = lambda a, b: list(set(a)&set(b))

# Write a program that adds the square of two numbers and prints it

a = 32
b = 21

result = a**2 + b**2
print(result)