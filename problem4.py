# create a class with a class attribute a; create an object from it and set 'a' 
# directly using object.a = 0. does this change  the class attribute


class demo:
    a = 4
o = demo()
print(o.a) # print the class attribute because instance attributr is not present
o.a = 3 #instane attribute is set
print(o.a) #print the istance attribute becuase instance attribute is present
print(demo.a)

    
