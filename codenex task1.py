def total():
    m=[]
    for i in range(1,6):
        marks=int(input("Enter you subject marks :"))
        m.append(marks)
        t=sum(m)
    print("THE TOTAL OF ALL SUBJECTS MARKS IS:",t)
def avg():
    m=[]
    for i in range(1,6):
        marks=int(input("Enter you subject marks :"))
        m.append(marks)
        t=sum(m)
    avgrage=t/len(m)
    print("THE AVGRAGE OF ALL SUBJECTS IS:",avgrage)
def grade():
    m=[]
    for i in range(1,6):
        marks=int(input("Enter you subject marks :"))
        m.append(marks)
        t=sum(m)
    avgrage=t/len(m)
    if avgrage >= 90:
        print("A+")
    elif avgrage >=80:
        print("A")
    elif avgrage >=70:
        print("B+")
    elif avgrage >=60:
        print("C+")
    elif avgrage >=50:
        print("C")
    elif avgrage >=40:
        print("D")
        

    
    else:
        print("F")
    

print("1.For total marks")
print("2.To get avg marks")
print("3.To get your grade")
a=int(input("Enter your choice:"))

if a==1:
    total()
elif a==2:
    avg()
elif a==3:
    grade()
else:
    print("PLEASE PUT 1,2,3")
