# ECE 2524 Homework 2 Problem 3 Arjun Passi

with open('account', 'r') as f:

    print "ACCOUNT SUMMARY"
    
    money = 0
    people = 0
    maxmoney = 0
    runTime = 0
    
    
    for line in f:
    
        myarray = line.split()

        startMoney = myarray[2]
        
        if maxmoney < float(startMoney):
            
            maxmoney = float(startMoney)
            nameMax = myarray[1]
            
        if runTime > 0:
        
            if minmoney > float(startMoney):
                minmoney = float(startMoney)
                name = myarray[1]
            
        else:
            minmoney = float(startMoney)
            name = myarray[1]
            
        money = money + float(startMoney)
        people = people + 1
        runTime = runTime + 1
        
    averageMoney = float(money/people)    
 
    print "Total amount owed = ",money
    print "Average amount owed = ",averageMoney
    print "Maximum amount owed = ", maxmoney, " by ", nameMax
    print "Minimum amount owed = ", minmoney, " by ", name
