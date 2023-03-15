import random
bruh = []
for i in range(12):
    bruh.append(random.randrange(1,11))

biggest = bruh[0]
for i in range(12):
    if bruh[i]>biggest:
        biggest = bruh[i]
print(bruh)
print("Biggest: ", biggest)
print()
print()
smallest = bruh[0]
for i in range(12):
    if bruh[i]<smallest:
        smallest = bruh[i]

print(bruh)
print("Smallest: ", smallest)

#bruh.sort()
#biggest = bruh[11]

bruh.sort(reverse = True)
print("Reversed: ", bruh)
print()
print()
bruh.sort()
print(bruh)
for i in range(10):
    if bruh[i]+1 == bruh[i+1]:
        if bruh[i+1]+1 == bruh[i+2]:
            print("The list contains ", bruh[i], bruh[i+1], bruh[i+2])



bruh2 = []
for i in range(12):
    bruh2.append(bruh[11-i])

print("Orginial list: ", bruh)
print("Reversed list: ", bruh2)
