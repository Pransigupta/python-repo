a =int(input("what,s the value of a ?"))
b = int(input("what's the value of b ?"))

if a>b :
    for i in range(1,10):
     print(a, "x", i, "=", a*i)
elif a<b :
      for i in range(1,10):
       print (b,"x", "=", b*i)

elif a==b :
    print ("nothing ")
else :
     print("stop")
    