#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: W0239497    
#Student Name:  Chauntel Smith

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Variable
    usageRate = 0
    #Welcome message & User Input Variable
    usage = float(input("Welcome, let us calculate your Usage Rate!\nEnter data usage in MB: "))
    #Usage calculateions
    if usage > 200 and (usage <= 500):
        usageRate = usage * 0.105
    elif usage > 500 and (usage <= 1000):
        usageRate = usage * 0.110
    elif usage > 1000:
        usageRate = 118
    else:
        usageRate = 20
    #Outcome message
    print("Your Total charge is: ${0:.2f}".format(usageRate))
    # YOUR CODE ENDS HERE

main()