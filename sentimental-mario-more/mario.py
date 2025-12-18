# TODO


from cs50 import get_int

# space = 1

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
for i in range(height):
    for space in range(height - i - 1, 0,-1):
            print(" ", end= "")
    for hash in range(i + 1):
        print("#", end= "")
    print("  ", end="")
    for right_hash in range(i+1):
        print("#", end= "")
    print("\n", end = "")








# if n > 0:

# for i in range(n):
#     print("#")
# a = 1
# # b = 0
# # d = 2


# for i in range(n):
#     print("#")


# while True:
#     try:
#         height = int(input("Height: "))
#         if (height >= 1) and (height <= 8):
#             break
#     except:
#         print("", end="")
# space = 1
# for i in range(height):

#     for space in range(height - i - 1, 0,-1):
#         print(" ", end= "")

#     for j in range(i + 1):
#         print("#", end= "")
#     print()