#name = input("What's your name?\n")
#print("name"[-1])

#print("Hi, " + name + ".")
#print("Hi, %s." % name)
#print("Hi,{0}." .format(name))
#print(f'Hi, {name}.')
#list = ['finger ' 'licking ' 'good.']
#print(','.join(list))
#print('{:,}'.format(1234567890))
#points = 6
#total = 220
#print('Correct answers: {:.03%}'.format(points/total))
#width=8
#print(' decimal      hex   binary')
# print('-'*27)
# for num in range(1,26):
#     for base in 'dXb':
#         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
#     print()
# d = datetime.datetime(2020, 7, 4, 12, 15, 58)
# print('{:%Y-%m-%d %H:%M:%S}'.format(d))
# a = "a"
# b = "b"
# an = "an"
# print(b + an)
# print(b + a*7)
# print(b + an*2 + a)
# print("$1" + ",000"*3)

# def compare(str1, str2):
#   return len(str1) == len(str2)


# print(compare("AB", "CD"))
# print(compare("ABC", "DE"))
# print(compare("hello", "App Academy"))

# def index_string(string):
#     return string[3:-1]

# print(index_string("Alchemy"))     #> hem
# print(index_string("Ridiculous"))  #> iculou
# print(index_string("Serendipity")) #> endipit

# string = "hello"
# string[0] = "H"

# print(string)
# def index_of(str, n):
#     return str.lower().index(n)

# print(index_of("Arm", "a"))  #> 0
# print(index_of("Pie", "e"))  #> 2
# print(index_of("Lucid", "i"))  #> 3
# print(index_of("Obvious","u"))  #> 5
# def is_last_character_n(str):
#     return str[-1] == "n"

# print(is_last_character_n("Aiden"))  #> True
# print(is_last_character_n("Piet"))   #> False
# print(is_last_character_n("Bert"))   #> False
# print(is_last_character_n("Dean"))   #> True

# def long_burp(n):
#     return "Bu" + ("r" * n) + "p"

# print(long_burp(3))  #> "Burrrp"
# print(long_burp(5))  #> "Burrrrrp"
# print(long_burp(9))  #> "Burrrrrrrrrp"

# def last_three(str1, str2):
#     return  str1[-3:].lower() == str2.lower()

# print(last_three("Power", "wer"))  #> True
# print(last_three("Application", "App"))   #> False
# print(last_three("Raw", "raw"))   #> True
# print(last_three("Bonjour", "OUR"))   #> True

# def is_palindrome(str):
#     reverse = ''.join(reversed(str))
#     return str == reverse

# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False

# def recursive_string(str):
#     if len(str) == 0:
#         return str

#     return recursive_string(str[1:]) + str[0]


# print(recursive_string("civic")) # civic
# print(recursive_string("refer")) # refer
# print(recursive_string("string")) # gnirts
# print(recursive_string("avocado")) # odacova
# print(recursive_string("application")) #

# Logical AND
# print(True and True)    # => True
# print(True and False)   # => False
# print(False and False)  # => False

# # Logical OR
# print(True or True)     # => True
# print(True or False)    # => True
# print(False or False)   # => False

# # Logical NOT
# print(not True)             # => False
# print(not False and True)   # => True
# print(not True or False)    # => False

# def is_same_num(a, b):
#     return a == b

# print(is_same_num(4, 8))   #>  False
# print(is_same_num(2, 2))   #>  True
# print(is_same_num(2, "2")) #>  False

# def not_equal(num1, num2):
#     return num1 != num2




# print(not_equal(0, 2))   #>  True
# print(not_equal(2, 2))   #>  False
# print(not_equal(2, "2")) #>  True
# def And(A, B):
#     return not A or B

# print(And(True, False))    #> False
# print(And(True, True))     #> True
# print(And(False, True))    #> False
# print(And(False, False))   #> False


# def length_list(A, n):
#     return len(A) == n

# print(length_list([], 1))   #>  False
# print(length_list([], 0))   #>  True
# print(length_list([5, 2], 2))   #>  True
# print(length_list([1, 4, 3], 4))   #>  False
# print(length_list([0, 2, "i", 0.9], 4))   #>  True

# def has_remainder(num1, num2):
#     return num1 % num2 != 0

# print(has_remainder(4, 2))   #>  False
# print(has_remainder(57, 4))  #>  True
# print(has_remainder(6, 3))   #>  False
# print(has_remainder(81, 7))  #>  True

# def xor(A, B):
#     return A ^ B

# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0

# def de_morgans_law(A, B):
#     return not (A and B)

# print(de_morgans_law(True, True)) # False
# print(de_morgans_law(True, False)) # True
# print(de_morgans_law(False, False)) # True
# print(de_morgans_law("", [])) # True
# print(de_morgans_law(2, 2)) # False
# print(de_morgans_law(2, 0)) # True

# print(7j)              # => 7j
# print(5.1+7.7j)    # => 5.1+7.7j
# print(complex(3, 5))    # => 3+5j
# print(complex(17))     # => 17+0j
# print(float(complex))       # => 0j
# print(float(17))        # => 17.0
# print(int(17.0))        # => 17

# x = 25
# y = 17.6
# print(x)
# print(y)
# print(x + y)
# print(x - y)

# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# # print(f" The result is {int(x // y)} remainder {int(x % y)}")
# print(x**2)
# print(y**2)
# print(float(x * y))

# def addition(num1, num2):
#     return num1 + num2
# print(addition(2, 3))   #> 5
# print(addition(-3, -6)) #> -9
# print(addition(7, 3))   #> 10

# def integer_division(x, z):
#     return (x // z)

# print(integer_division(5.0, 2))     #> 2.0
# print(integer_division(10, 10))     #> 1
# print(integer_division(60, 8.0))    #> 7.0
# print(integer_division(5.0, 1.0))   #> 5.0
# print(integer_division(8, 2))       #> 4

# def find_digit_amount(x):
#     l = len(str(x))
#     if x < 0:
#         return l - 1
#     return l

# print(find_digit_amount(123))           #> 3
# print(find_digit_amount(-56))           #> 2
# print(find_digit_amount(7154))          #> 4
# print(find_digit_amount(61217311514))   #> 11
# print(find_digit_amount(0))             #> 1

# def perfect_square(x, y):
#     return x / y == y and y *  y == x

# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False


# def recursive_fib(z):
#     if z <= 1:
#         return z
#     else:
#         return (recursive_fib(z-1) + recursive_fib(z-2))

# print(recursive_fib(1))     #> 1
# print(recursive_fib(2))     #> 1
# print(recursive_fib(4))     #> 3
# print(recursive_fib(6))     #> 8
# print(recursive_fib(12))    #> 144

# def recursive_countdown(g):
#     if g <= 0:
#         return
#     else:
#         print(g)
#         recursive_countdown(g-1)


#     recursive_countdown(5) #> 5 4 3 2 1

# def is_prime(num , i =2):
#     if (num <= 2):
#         return True if (num == 2) else False
#     if (num % i == 0):
#         return False
#     if (num < i * i):
#         return True
#     return is_prime(num, i + 1)

# print(is_prime(1))  #> False
# print(is_prime(2))  #> True
# print(is_prime(3))  #> True
# print(is_prime(5))  #> True
# print(is_prime(9))  #> False
# print(is_prime(15)) #> False



# a = 4
# b = 5
# print( not a == b
# print(slowValidation() or skip)
# print(skip or slowValidation())
# print (a == b)

# import pyttsx3

# engine = pyttsx3.init()
# name = input("What's your name? ")
# engine.say(f"hello, {name}")
# engine.runAndWait()

# def divisible_by_five(x):
#     return x % 5 == 0

# print(divisible_by_five(5))    #> True
# print(divisible_by_five(-55))  #> True
# print(divisible_by_five(37))   #> False

# def calculate_exponent(x, y):
#     return x**y

# print(calculate_exponent(5, 5))     #> 3125
# print(calculate_exponent(10, 10))   #> 10000000000
# print(calculate_exponent(3, 3))     #> 27

# def remainder(x, z):
#     return x % z
# print(remainder(1, 3))  #> 1
# print(remainder(3, 4))  #> 3
# print(remainder(5, 5))  #> 0
# print(remainder(7, 2))  #> 1


# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

#print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

# print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))
#> False

