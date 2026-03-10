 # Left incremental pyramid
# count=int(input("Enter Row Number= "))
# for i in range(count):
#     for j in range(i+1):
#         print("*",end="")
#     print()

 # Left decrement pyramid
# count=int(input("Enter Row Number= "))
# for i in range(count):
#     for j in range(count,i,-1):
#         print("*",end="")
#     print()

# Right Incremental Pyramid 
# count=int(input("Enter Row Count= "))
# for i in range(count):
#     for k in range(count,i,-1):
#         print(end=" ")

#     for j in range(i+1):
#         print("*",end="")
#     print()

# Right Dicremental Pyramid 
# count = int(input("Enter Row Count = "))
# for i in range(count): 
#     for k in range(i):
#         print(" ", end="")
#     for j in range(count - i):
#         print("*", end="")
#     print()

# Hill-decrimental pyramid
count = int(input("Enter Row Count = "))
for i in range(count): 
    for k in range(i):
        print(" ", end="")
    for j in range(count,i,-1):
        print("*", end=" ")
    print()

