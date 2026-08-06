s=set()
s.add(20)
s.add(20.0) #numerically value of 20 and 20.0 is same so only one value will be stored in the set
s.add('20')

print(len(s))