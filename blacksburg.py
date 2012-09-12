# ECE 2524 Homework 2 Problem 2 Arjun Passi

with open('account', 'r') as f:

    print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
    
    for line in f:
        value = line.split()
        
        if "Blacksburg" in value:
        
            ans = value[4],value[1],value[0],value[3]
            
            comma = ", "
            
            print comma.join(ans)
            
            
