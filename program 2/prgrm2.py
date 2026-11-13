num_list=[-5,10,30,-45,-3,33,-12,24]
print(num_list)
newlist=[x for x in num_list if x>0]
print("the positive numbers are:",newlist)


#sqare numbers

n=int(input("enter the number of elements:"))
num_list=[]
for i in range(n):
    a=int(input("enter the numbers:"))
    num_list.append(a)
print("entered list:",num_list)
sqr_lst=[x**2 for x in num_list]
print("squared list:",sqr_lst)


    #vowels

word=input("enter a word:")
vowels=[x for x in word.lower()if x in['a','e','i','o','u']]
print("the vowels in the words are:",vowels)


    #ordinal value


w=input("enter a word:")
ord=[ord(x)for x in w]
print("the ordinal value is:",ord)
