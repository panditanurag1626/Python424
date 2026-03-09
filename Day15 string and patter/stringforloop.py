# Iterate string
name="Itvedant"
# for i in name:
#     print(i)

# reverse string
# print("reverse string:",name[::-1])

# newstr=""
# for i in name:
#     newstr=i+newstr

# print(newstr)

# wap newstring without vowels

# without_vowel_str=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         without_vowel_str=without_vowel_str+i

# print(without_vowel_str)


# wap to print number of accurances of entered charactor or word from any string

str=input("Enter String=") #welcome
checkstr=input("Enter Char/Word to find and show count=")
count=0
check=""
for i in range(len(str)):
    #print(i,str[i])
    k=i
    for j in range(len(checkstr)):
        try:
            checkstr=str[k]
            k+=1
        except:
            None
    if check==checkstr:
        count+=1
        check=""

if count!=0:
    print(f"{checkstr} found in {str} and count={count}")
else:
    print(f"{checkstr} not found in {str}")