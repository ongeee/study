# Baekjoon Online Judge

# 20210125

# 6-1 (15596) [RE]
def SUM(M):
    
    S = 0
    for i in (M):
        S = S + i
        
    return S

# 6-2 (4673)
results = []
for i in range(10000):
    
    S = i + sum(list(map(int, str(i))))
    
    results.append(S)
    
for i in range(10000):
    
    if (results.count(i) == 0):
        print(i)
        
# 6-3 (1065) [RE]
N = input()
N = int(N)

if (N<100):
    print(N)
    
else:
    
    num = 99
    for i in range(100,N+1):
    
        sep = list(map(int, str(i)))
        
        sub_1 = sep[1] - sep[0] 
        sub_2 = sep[2] - sep[1]  
        
    
        if ((sub_1) == (sub_2)):
            num = num+1
        else: num = num
            
    print(num)
    
    

