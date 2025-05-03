#title
print ("hello ")
print ("My name is Mohamed")
print ("my age 23 ")
print ("Student at faculty of infromation tecnology")

#numbers 
"""في الارقام الاولوية للاقواس ولو مفيش اقواس الاولية معروفة للعمليات الكبيرة """
a =8 +2 * 10 
print ("a = " , a)

b = (8+2)*10
print ("b = ", b) 

c = 18/4 
print ("c = ", c)

c1 = 18 //4 
print ("c1 = ", c1)

c2 = 18%4 
print ("c2 = ", c2)

d = 5*5*5
print ("d = " , d)

d1 = 5**3
print ("d1 = " , d1) 

#variables
"""في متغيرات نقدر نخزن فيها رقم وبعدين متغير نجمعه معى رقم جديد ونقدر نخزن ارقام في زوز متغيرات ونجمعهم معى بعض ويعطوني ناتج رقم صحيح"""
rocky = 5 
print ("rocky = " , 5 + rocky )

baila = 20 
baila + rocky
print ("BailaRocky " , baila + rocky)

#string 
"""السترنق ضروري تكون بين  علامتين تنصيص "like this " وهكي تكون"""

z = "Summer time sadnis"
print (z) 

#لما نبي  ندير سترنق في سنقل كوت ولاكن الكلمة فيها اختصار زي مموضح اسفل
#  'i don't know '

#فا الحل ضروري نديرهم بين دبل كوت "" ونكتب الكلمة عادية 
"i don't know "

#وحل اخر نستخدم باك سلاش /

x = 'i dont know '
print (x)

#قبل سلسلة r نقدر نخلي اي حرف بعد باك سلاش مليشي اهمية بأضافة حرف 
print ("c:desctop\dior\home\nyouGreate")
print (r"c:desctop\dior\home\nyouGreate")

#نقدر نجمع السلاس زي الارقام 
firstName = " Mohamed"
firstName = firstName + " Assed" 

print(firstName)

#نقدر نضرب حتى السلاسل في بعض وناتج يكررلي السلسلة حسب الرقم المضروب فيه

print (firstName * 3)

#الوصول ل عناصر في السلسة 
user = "mohamed assed"
print (user[0])
print(user[1])

#نقدر نوصل لاخر عنصر في السلسلة عن طريق  -1
print(user[-1])

# [2:9] نقدر نطبيع جزء معين من سلسلة عن طريق 
print (user[2:9])

#طباعة طول سلسلة
print (len(user))

# list المصفوفات او 
players = [19 , 11 , 9 , 7 , 5 ]
print (players[2])

#نقدر نغير اي عنصر في مصفوفة بالطريقة التالية 
players [2] = 10
print (players[2])

#طباعة مصفوفة كاملة 
print (players)

#اضافة عناصر في نهاية المصفوفة  
# تعني افعل شي ما للمصفوفة .
# append اضافة
players.append(99)
print(players)

#if statemnt

age = 23
if age <= 20 :
    print ("you can't buy this bequse you ander 20")
elif age >= 20 :
    print ("you can buy yhis")

# if statemnt in string

name = "proten"

if name is "proten":
    print ("i love you proten")
elif name is "any one":
    print ("go away")
else:
    print ("please enter right name hehe")


# for loop
foods = ["tuna" , 'fish' , 'meat' , 'chicken'  ]
for f in foods :
    print (f)
    print (len(f))

print ("")
for x in range (10):
    print (x)


for i in range (5):
     print("you'r grate you'r the best")

for i in range (10 , 55 , 5):
    print(i)

# while loop 

Golden = 1
while Golden < 10:
    print ("you'r the best")
    Golden +=1
    
# Escape Sequences characters
# \b => back spaec
# \  newline => Escape New line + \
# \\ => Escape back Slash
# \' => Escape single qoute
# \" => Escape double qoutes
# \n => new line
# \r => carriage return
# \t => horizontal tab 
# \xhh => character with hex value hh


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