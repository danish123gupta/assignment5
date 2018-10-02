#q.no.1
year=int(input("enter a year to check it is leap year or not:"))
if year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")

#q.no.2
length=int(input("enter length:"))
breadth=int(input("enter breadth:"))
def dimensions(l,b):
    if l==b:
        return("dimensions of square")
    else:
        return ("dimensions of rectangle")
print(dimensions(length,breadth))


#q.no.3
p1=int(input("enter the first age of a person:"))
p2=int(input("enter the age of second person:"))
p3=int(input("enter the age of third person:"))
old_person=max(p1,p2,p3)
youngest_person=min(p1,p2,p3)
print("the oldest of the three person is:",old_person)
print("the youngest of the three person is:",youngest_person)


#q.no.4
emp_age=int(input("enter the age:"))
emp_sex = str(input("enter the sex(M or F):"))
emp_status = str(input("enter the martial status(Y or N):"))
if(emp_sex==('F')):
    print("she will work in urban areas")
elif(emp_sex==('M'))and (20<=emp_age<40):
    print("he work in anywhere")
elif(emp_sex==('M'))and (40<=emp_age<60):
    print("he will work in urban areas")
else:
    print("ERROR!!!!")

#Q.NO.5
qt=int(input("enter the quantity of items to buy:"))
cost=(qt*100)
if cost>1000:
    discount=(cost)*.10
    cost-=discount

    print("the cost of the iem is:",cost)
else:
    print("the cost of item is:",cost)

#Q.NO.6
x=[]
for i in range(10):
    x.append(input("enter a number:"))
    print(x,sep='\n')
#Q.NO.7
while True:
    print("infinite loop")

#q.no.9
l=[1,"danish",3,5]
l1=[]
l2=[]
l3=[]
for i in l:
    if type(i)==int:
        l1.append(i)
        print(l1)
    elif type(i)==int:
        l2.append(i)
        print(l2)
    else:
        l.append(i)
        print(3)

 #Q.N0.10
l=[]
for i in range(1,101):
     if i>1:
         for j in range(2,i):
             if i%j==0:
                 break
     else:
         l.append(i)
print(l)

#q.no.11
for i in range(1,5):
    print("* *i")


#Q.NO.12
n=int(input("enter total number of elements:"))
l=[]
for i in range(n):
    n1=int(input("enter number:"))
    l.append(n1)
print(l)
n2=int(input("enter element to be searched:"))
for j in 1:
    if j==n2:
        k=l.index(j)
        l.pop()
print(l)




