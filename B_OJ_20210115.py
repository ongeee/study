# Baekjoon Online Judge


# 20210115

# 1-9 (10869)
A, B = input().split()
A = int(A)
B = int(B)

print(int(A+B))
print(int(A-B))
print(int(A*B))
print(int(A/B))
print(int(A%B))

# 1-10 (10430)
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print(int((A+B)%C))
print(int(((A%C)+(B%C))%C))
print(int((A*B)%C))
print(int(((A%C)*(B%C))%C))

# 1-11 (2588) [RE]
A = input()
B = input()

A = int(A)
B = int(B)

c = int(B%10)
b = int((B/10)%10) 
a = int((B/100))

Ac = A*c
Ab = A*b
Aa = A*a

print(int(Ac))
print(int(Ab))
print(int(Aa))
print(int(Ac+(10*Ab)+(100*Aa)))

