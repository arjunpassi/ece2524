# ECE 2524 Homework 2 Problem 1 Arjun Passi
with open('/etc/passwd', 'r') as f:
    # or read it line by line
    for line in f:
        value = line.split(":")
        
        print value[0], '\t',  value[6]
