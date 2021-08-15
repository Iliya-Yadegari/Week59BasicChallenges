def perfect(num):
    total = 0
    
    for i in range(1, num):
        if num % i == 0:
            total = total + i
            
    if total == num:
        return True
    else:
        return False

for i in range(1,1000):
    if perfect(i) == True:
        print(i)