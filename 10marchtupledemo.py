# Create tuple
tup=()
print(tup,type,(tup))
t1=tuple()
print(t1,type(t1))

t2=(500)
print(t2,type(t2))

t3=(500,100,"hello",True,5j,89.8789)
print(t3,type(t3))

# t4=tuple(78,89,90) #error
t4=tuple((78,89,90)) 
print(t4,type(t4))

my_tuple=(3,45,64,6764,34,100)
print(my_tuple)

# Index
print("First Element= ",my_tuple[0])
print("Last Element= ",my_tuple[-1])

# Slicing
print(my_tuple[::-1])
print(my_tuple[2:5])

# Operation
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
#print(tuple1+100) # TypeError: can only concatenate tuple (not "int") to tuple

# Tuple Funcation
tuple3=(1,5,4,2,3)
print(tuple3)
print(sorted(tuple3))
print(sorted(tuple3)[::-1])
print(sorted(tuple3,reverse=True))


# Tuple Method-index(),count
tuple4=("hello","red","orange","green",1000,300,700)
#print(tuple4.index(3)) # If element not present then valueErroe
print(tuple4.index(300))
print(tuple4.count(300))

# Immutabilty
tuple4[0]="welcome" # TypeError: 'tuple' object does not support item assignment
print(tuple4)