def perm3(word):
    list3=[]
    c1=word[0:1]
    c2=word[1:2]
    c3=word[2:3]
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    return list3
#perm3('EAT')
word='FAST'
def perm4(word):
    
    c1=word[0:1]
    c2=word[1:2]
    c3=word[2:3]
    c4=word[3:4]
    list4=[]

    part1=c1
    part2=c2+c3+c4
    list3=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+list3[i])

    part1=c2
    part2=c1+c3+c4
    for i in range(0,6,1):
        list4.append(part1+list3[i])

    part1=c3
    part2=c1+c2+c4
    for i in range(0,6,1):
        list4.append(part1+list3[i])

    part1=c1
    part2=c1+c2+c3
    for i in range(0,6,1):
        list4.append(part1+list3[i])
        
    print(list4)
perm4('FAST')
