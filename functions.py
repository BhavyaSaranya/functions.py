# String transform functions
#capitalize
data="my name is bhavya"
print(data.capitalize())

#upper
name="bhavya"
print(name.upper())

#lower
name="SARANYA"
print(name.lower())

#title
name="bhavya saranya"
print(name.title())

#casefold
name="bHAVYA25"
print(name.casefold())

#swapcase
name="bhavya varma"
print(name.swapcase())

#string check functions
#isnumeric
a="53421"
print(a.isnumeric())

#isalpha
a="vaishu"
print(a.isalpha())
a="vaishu06"
print(a.isalnum())

#isdecimaL
a="56.5"
print(a.isdecimal())

#isdigit
a="777"
print(a.isdigit())

#isascii
a="bhavya76"
print(a.isascii())

#isupper
name="bhavya"
print(name.isupper())

#islower
name="saranya"
print(name.islower())

#isspace
a="bhavya"
print(a.isspace())

#issprintable
a="bhavya@varma25"
print(a.isprintable())

#isidentifier
a="saranya_bhavya"
print(a.isidentifier())

#crud functions
#append
lst=[]
lst.append("bhavya")
lst.append("saranya")
print(lst)

#insert
a=["bhavya","saranya"]
a.insert(1,"varma")
print(a)

#read
names=["a","b"]
print(names.index("b"))

#count
names=["a","b","c","a"]
print(names.count("a"))

#extend
names=["a","b","c","d"]
nums=["4","6","7"]
names.extend(nums)
print(names)

#remove
names=["a","b","c","d"]
names.remove("b")
print(names)

#pop with index
names=["bhavya","saranya","malika"]
names.pop(1)
print(names)

#pop without index
names=["bhavya","saranya","malika"]
names.pop()
print(names)

#clear
names=["bhavya","saranya","malika"]
names.clear()
print(names)

#sort
num=[1,8,9,6,7,4]
num.sort()
print(num)

#reverse
num=[1,8,9,6,7,4]
num.reverse()
print(num)



