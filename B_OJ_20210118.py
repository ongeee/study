# Baekjoon Online Judge


# 20210118

# 2-1 (1330)
A, B = input().split()
A = int(A)
B = int(B)

if (A>B):
    print('>')
    
elif (A<B):
    print('<')
        
else: print('==')

# 2-2 (9498)
score  = input()
score = int(score)

if (score>=90):
    print('A')
    
elif (score>=80):
    print('B')
    
elif (score>=70):
    print('C')
    
elif (score>=60):
    print('D')
    
else: print('F')

# 2-3 (2753)
year = input()
year = int(year)

if (((year%4)==0)and((year%100)!=0)) or (((year%4)==0)and((year%400)==0)):
    print('1')
    
else: print('0')

# 2-4 (14681) [RE]
A = input()
B = input()

A = int(A)
B = int(B)

if (A>0) and (B>0):
    print('1')
    
elif (A>0) and (B<0) :
    print('4')
    
elif (A<0) and (B>0):
    print('2')
    
else: print('3')
 
# 2-5 (2884)
H, M = input().split()

H = int(H)
M = int(M)

if (M>=45):
    print(H, int(M-45))
    
elif (H==0):
    print('23', int(M+60-45))
    
else: print(int(H-1), int(M+60-45))
