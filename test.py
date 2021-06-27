#!/uer/bim/Python2.7

n = int(input())
seed = 0
# Code Time
while n<=1:
    if (n%2 == 0): # 如果n是偶数
        n /= 2
    else:          # 如果n是奇数
        n = (3*n+1)/2 
    
    seed += 1

print(seed)