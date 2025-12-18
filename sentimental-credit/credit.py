# TO DO
from cs50 import get_string
from cs50 import get_int

# def main():
#     while True:
#         card_cardNO = get_int("Number: ")
#         if card_cardNO >= 0:
#             break

#     if check_valid(card_cardNO):
#         print_credit_card_type(card_cardNO)
#     else:
#         print("INVALID")

# def check_valid(cardNum):
#     return checksum(cardNum)

# def checksum(cardNum):

#     sum = 0
#     for i in range(len(str(cardNum))):
#         if (i % 2 == 0):
#             sum  += cardNum % 10
#         else:
#             num = 2 * (cardNum % 10)
#             sum += num // 10 + num % 10

#             cardNum //= 10
#         return sum % 10 == 0


# def print_credit_card_type(cardNum):

#     if (cardNum >= 34e14 and cardNum < 5e12) or (cardNum >= 4e15 and cardNum < 5e15):
#         print("AMEX")
#     elif (cardNum >= 51e14 and  cardNum < 56e14):
#         print("MASTERCARD")
#     elif (cardNum <= 4e12 and cardNum < 5e12) or (cardNum >= 4e15 and cardNum < 5e15):
#         print("VISA")
#     else:
#         print("INVALID", end="")


# credit = get_string("Number: ")
# credit_no = credit[::-1]
# total_card = sum ( [(int(x) * 2) // 10 + ((int(x) * 2) % 10) for x in credit_no[1::2]] ) + sum ( [int(x)for x in credit_no[0::2]] )

# if total_card % 10 == 0:
#     if len(credit) == 15 and credit[0:2] in [ '34', '37']:
#         print('AMEX')
#     elif len(credit) == 16 and 51 <= int(credit[0:2]) <= 55:
#         print('MASTERCARD')
#     elif len(credit) in [13, 16] and credit[0] == '4':
#         print('VISA')
#     else:
#         print("INVALID")
# else:
#     print("INVALID")


from cs50 import get_int
import sys
number = get_int("Number:" )
even = 0
two_digit = 0 # This will store the last two digits
i = 0 # This is to count the amount of digits in the credit card number, and while the function is going on we can see if the number is odd or even.
oddsum = 0 # This number by the end of the while function will end up adding all the oddnumbers from right to left
evensum = 0 # This number by the end of the while function will end up adding all the evennumbers from right to left
while number > 0:
    if i % 2 == 0:
        j = number % 10
        oddsum += j
        i = i + 1
    else:
        j = number % 10
        j *= 2
        if j >= 10:
            a = j % 10
            b = j // 10
            evensum += a + b
            i = i + 1
        else:
            evensum += j
            i = i + 1
    number //= 10
    return evensum % 10 != 0
/workspaces/111929680/smiley
if number > 9 and number < 100:
    two_digit = number
    print(two_digit)
    evensum = evensum + oddsum

    print("INVALID")
    sys.exit(0)
if i == 16 or 13:
    if (two_digit == 40 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48 or 49):
        print("VISA")
        sys.exit(1)
elif i == 16:
    if two_digit == 51 or 52 or 53 or 54 or 55:
        print("MASTERCARD")
        sys.exit(1)
elif i == 15:
    if two_digit == 34 or 37:
        print("AMEX")
        sys.exit(1)
else:
    print("INVALID")
    sys.exit(1)