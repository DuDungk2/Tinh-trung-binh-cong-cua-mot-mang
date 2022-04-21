while True:
    try:
        n=int(input('Nhap m: '))
        break;
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập số nguyên.')
m=[]
so_chan= []
so_le= []
for i in range(n):
    m = m+ [  int(input('Nhap m[%d]='%i))   ]


for i in range (n) :
    if m[i]%2==0:
        so_chan.append(m[i])
    else:
       so_le.append(m[i])
     
s=0
for i in range (n) :
    if m[i]%2==0:
        s= s + m[i]




print('Cac so chan la:',so_chan)
print('Cac so le la:',so_le)
print('Trung bình cộng= ', s/len(so_chan))
    
