import re, math
instance = 1

if __name__ == '__main__':

    n = int(input("enter the number of minutes: "))

    utilization =[]

    for i in range(n):
        s = input("enter the utilization: ")
        utilization.append(int(s))
    
    i = 0

    while i < n:
        
        if utilization[i] < 25:
            instance = math.ceil(instance / 2)
            i += 11  
        
        elif utilization[i] > 60:
            if instance * 2 <= 2 * 10**8:
                instance = instance * 2
            i += 11  
        
        else:
            i += 1

    print(instance)