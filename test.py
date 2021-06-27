#!/uer/bim/Python2.7
import Time
import os

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
time.sleep(1)
print("[          ]0% ")
time.sleep(1)
print("[=====     ]50%")
time.sleep(1)
print("[==========]100%")
time.sleep(1)
print("----------")
time.sleep(0.5)
print(n)