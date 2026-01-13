from unittest import case

num=4
if num%2==0:
    print("even number")
else:
    print("odd number")
marks=80

if marks>=90:
    print("grade a")
elif marks>=80:
    print("grade b")
else:
    print("grade c")

for i in range(1,6):
    print(i)

    j=1
while j<=5:
    print(j)
    j+=1
    if j==2:
        break

day=2
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")

