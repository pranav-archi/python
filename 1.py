def convert1(fname):    
    f1=open(fname,'r')
    list1=fname.split('.')
    f2=open(list1[0]+'_out.'+list1[1],'w')
    for i in range(0,3,1):   
        info1=f1.readline().replace('\n','')
        print(info1)
        list1=info1.split(' ')
        lhs_value=float(list1[0])
        lhs_units=list1[1]
        rhs_value=float(list1[3])
        rhs_units=list1[4]
        line1=str(str(1)+' '+lhs_units+' = '+str((rhs_value/lhs_value))+' '+rhs_units)
        line2=str(str(1)+' '+rhs_units+' = '+str((lhs_value/rhs_value))+' '+lhs_units)       
        f2.write(line1+'\n'+line2+'\n'+'\n')
    f2.close()
convert1('convert.txt')
