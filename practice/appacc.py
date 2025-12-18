# To take input from the user
num = int(input("Enter a number: "))

# By definition, prime numbers are greater than 1
if num > 1:
  # check for factors
  for i in range(2,num):
    # check for remainder in division (mod), if none it's not prime
    if (num % i) == 0:
      print(num,"is not a prime number")
      # find it's corresponding factor using integer division
      print(i,"times",num//i,"is",num)
      break
  else:
    print(num,"is prime")

else:
  print(num,"is not a prime number")