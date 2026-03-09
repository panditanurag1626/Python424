# for i in range(3):
#     print("*")
# r=3
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("*",end="")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("i",end="")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("j",end="")
#     print()


# row=int(input("Enter Row Count="))
# column=int(input("Enter Column Count"))
# for i in range(row):
#     for j in range(column):
#         print("*",end="")
#     print()


# row=int(input("Enter Row Count="))
# column=int(input("Enter Column Count"))
# for i in range(row):
#     for j in range(column):
#         if i==j:
#             print("1",end="")
#         else:
#             print("0",end="")
#     print()


# Left Incremental Tringle
count = int(input("Enter Row Count= "))
for i in range(count):
    for j in range(i+1):
        print("*",end="")
    print()

count = int(input("Enter Row Count= "))
for i in range(count):
    for j in range(i+1):
        print(i,end="")
    print()



count = int(input("Enter Row Count= "))
n=1
for i in range(count):
    for j in range(i+1):
        print(n,end="")
        n+=1
    print()