a=[]
p= int(input("Enter the total no. of terms: "))
for i in range(p):
    b=int(input("Enter num"+str(i+1)+": "))
    a.append(b)
print(a)

sum=0
for i in a:
    sum=sum+i
print("The sum is : ",sum)

avg=sum/(len(a))
print("Average is : ",avg)
