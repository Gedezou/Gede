# # DO NOT EDIT - Setup for exploration
# # tiny number
# int1 = 5
# float1 = 5.0
# # small number
# int2 = 135
# float2 = 135.246
# # huge number known as `googol`
# int3 = 10**100
# float3 = 10.0**100

# # STEP 1: Print and compare tiny numbers
# print('** FIVE **')
# print(int1)
# print(float1)
# print(int1 == float1)
# # 1A: Print int1
# # 1B: Print float1
# # 1C: Print equality comparison (==) between int1 and float1

# # STEP 2: Print and compare huge numbers
# print('\n** GOOGOL **')
# print(int3)
# print(float3)
# print(int3 == float3)
# # 2A: Print int3
# # 2B: Print float3
# # 2C: Print equality comparison (==) between int1 and float3

# # STEP 3: Compare results of integer division in all 4 possible combinations
# print('\n** INTEGER DIVISION **')
# print(int2 // int1)
# print(float2 // float1)
# print(float2 // int1)
# print(int2 // float1)
# print(int2 // float1)

# # 3A: Print int2 divided by int1 (//)
# # 3B: Print float2 divided by float1 (//)
# # 3C: Print float2 divided by int1
# # 3D: Print int2 divided by float1

# # STEP 4: Compare results of mod in all 4 possible combinations
# print('\n** MOD **')
# print('\n** INTEGER DIVISION **')
# print(int2 % int1)
# print(float2 % float1)
# print(float2 % int1)
# print(int2 % float1)
# # Copy/paste 4 statements from STEP 3 and switch operator to mod (from // to %)

# def increment(A):
#     return A + 1


# print(increment(0))   #> 1
# print(increment(9))   #> 10
# print(increment(-3))  #> -2

# def min2sec(x):
#     return x * 60

# print(min2sec(5)) #> 300
# print(min2sec(3)) #> 180
# print(min2sec(2)) #> 120

# def how_many_legs(x, y, z):
#     return (x*2 + y*4 + z*4)

# print(how_many_legs(2, 3, 5))    #> 36
# print(how_many_legs(1, 2, 3))    #> 22
# print(how_many_legs(5, 2, 8))    #> 50

def string_int(x):
    return int(x)

print(string_int("6"))     #> 6
print(string_int("1000"))  #> 1000
print(string_int("12"))    #> 12