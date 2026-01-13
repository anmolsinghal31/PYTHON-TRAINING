add=lambda a,b :a+b
print(add(3,5))
mul=lambda c,d : c*d
print(mul(100,20))
maxnum=lambda x,y : x if x>y else y
print(maxnum(10,40))
#map function
numbers=[1,2,3,4,5,6,7,8,9,10]
result=map(lambda x:x*2,numbers)
print(list(result))