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