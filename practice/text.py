text = "In the great green room"
words = text.split()

# Round 1 fight
print("Round 1")
for word in words:
    print(word)
print()

#Round 2 Go again!
print("Round 2")
for word in words:
    for c in word:
        print(c)
print()
# Round 3 Yes!!
print("Round 3")
for word in words:
    if "g" in word:
        print(word)
print()

# Round $ Teehhe!
print("Round 4")
for word in words[2: ]:
    print(word)
print()

# Round cinco
print("Round 5")
for _ in words:
    print("Goodnight Moon")
print()
