
'''
self maths test
'''
q= "321"
print("self testing begins in...")
for character in q:
    print(character)

a=int(input("enter first number:")) 
b=int(input("enter second number:"))
c="continue"
d="try again"
print("what\'s", a, "+", b, "?")
e=int(input("enter your answer:"))
print("what\'s", a, "-", b, "?")
f=int(input("enter your answer:"))
print("what\'s", a, "/", b, "?")
g=input("enter your answer:")
print("what\'s", a, "*", b, "?")
h=int(input("enter your answer:"))
i="there is a scope in farming too"
if a+b==e and a-b==f and a/b==float(g) and a*b==h: print(c, end=" and no need to ") #pass
if a+b==e or a-b==f or a/b==float(g) or a*b==h: print(d) #fail
else: print(i) #dumb