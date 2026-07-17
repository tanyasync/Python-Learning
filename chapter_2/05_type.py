a=76
t=type(a) #class <int>
print(t)

a="tanya"
t=type(a) #class <str>
print(t)

a="76"
t=type(a) #class <str>
print(t)

a="98"
b=float(a) #but the type should be float
t=type(b) #class <
print(t)

# str(31)=>"31" integer to string conversion
# int(31)=>"31" string to integer conversion
# float(31)=>"31" integer to float conversion

h=65
g=str(h)
t=type(g)
print(t)