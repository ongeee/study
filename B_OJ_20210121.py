# Baekjoon Online Judge

# 20210121

# 4-1 (10952)
A, B = input().split()

A = int(A)
B = int(B)

while ((A!=0) and (B!=0)):
    
   print(int(A+B))    
   
   A, B = input().split()
    
   A = int(A)
   B = int(B)
    

# 4-2 (10951) [RE]
A, B = input().split()

A = int(A)
B = int(B)   
   
while True:
    
   try:
       print(int(A+B))
       
       A, B = input().split()
       
       A = int(A)
       B = int(B)
   
   except: 
       break

# 4-3 (1110)
N = input()
N = int(N)

result = N
loop_num = 0
while (result != N) or (loop_num ==0):

    try: 
        sum_num = int(result//10) + int(result%10)
        new_num = int('%d' %(result%10) + '%d' %(sum_num%10))
    
        result = new_num
    
        loop_num = loop_num + 1
        
    except:
        break
    
print(int(loop_num))
        
        
        
