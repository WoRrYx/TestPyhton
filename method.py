# strip() remove spaces from start and end of string
# rstrip() remove spaces from end of string
# lstrip() remove spaces from start of string

a = "    Hello World    "
print(a.strip()) # remove spaces from start and end of string
print(a.rstrip()) # remove spaces from end of string
print(a.lstrip()) # remove spaces from start of string

b = "#@Hello World@#"
print(a.strip('@#')) # remove #@ from start and end of string
print(a.rstrip('@#')) # remove #@ from end of string
print(a.lstrip('@#')) # remove #@ from start of string


# title case () => convert first letter of each word to upper case

f = "ilove 2d graphic and 3g technology and pyhthon"
print(f.title()) # convert first letter of each word to upper case

# title capitalize() => convert first letter of string to upper case
h = "ilove 2d graphic and 3g technology and pyhthon"
print(h.capitalize()) # convert first letter of string to upper case

# zfill() => fill string with 0 to make it 10 characters long

a , b ,c = 1 , 11 , 111
print (a)
print (b)
print (c)

print (str(a).zfill(3)) # fill string with 0 to make it 3 characters long
print (str(b).zfill(3)) # fill string with 0 to make it 3 characters long
print (str(c).zfill(3)) # fill string with 0 to make it 3 characters long

# upper and lower function

r = "mohamed"
print (r.upper())

q = "DANIA"
print(q.lower())

#split rsplit 

e = "i love pyhton and php"
print (e.split())
print (e.rsplit())

# center 

e = "Mohamed" 
print (e.center(9)) # spaces
print (e.center(9, "#")) # hashes


# clear() => remove all elements from list

BCAA= [1, 2, 3, 4, 5]
print (BCAA) # [1, 2, 3, 4, 5]
BCAA.clear() # remove all elements from list