n1=0
n2=1
count=0
last_number= int(input('How many terms do you want? '))
while count<last_number:
    print(n1)
    fn= n1+n2
    # update values
    n1=n2
    n2=fn
    count=count+1
