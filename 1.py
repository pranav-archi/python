f1=open('convert.txt','r')
for i in range(0,3,1):   
    info1=f1.readline().replace('\n','')
    print(info1)
    list1=info1.split(' ')
    lhs_value=float(list1[0])
    lhs_units=list1[1]
    rhs_value=float(list1[3])
    rhs_units=list1[4]
    print(1,lhs_units,'=',(rhs_value/lhs_value),rhs_units)
    print(1,rhs_units,'=',(lhs_value/rhs_value),lhs_units)
    print()
