def genPrimes():
    num = 2
    prev = []  
    while True:
        for p in prev:    
            if num % p == 0:
                break
        else:
            prev.append(num)
            yield num
        num += 1
