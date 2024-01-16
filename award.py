""" 
******Pseudo code******
The program wil take the time of swimming, cycling and running from user as input 
It will use the float function to convert the data into float taken by user as the time can be given in points
Than it will add the time of swimming , running and cycling into a variable
Than program will display the total taken by swimming, cycling and running by using print function
program will use if elif conditional and logical operator structure to compare the total taken by player and the time set to get award
While comparing the time taken by player if it matches with the conditionit will go inside the condition body and display the message that what player got as aaward or get nothing 
"""


#take the time taken by swimming from user
swimming=float(input("Please enter the time taken by swimming"))
#take the time taken by cycling from user
cycling=float(input("Please enter the time taken by cycling"))#
#take the time taken by running from user
running=float(input("please enter the time taken by running"))
#Add the time of swimming,cycling and running and save into variable named total
total = swimming + cycling + running
#Print the total taken by plyer to complete the triathlon
print("Total time taken by Triatholn", total)
#if will compare the total with the time set to get the award and than print message accordingly
if (total >= 0) and (total <= 100 ):
    print("Congragulationns! Player is awarded by provincial colours")
elif (total >= 101) and (total <= 105):
    print("Player is awarded by provincial half colours")
elif (total >= 106) and (total <= 110):
    print("Provincial scroll")
elif (total >= 111):
    print(" No awards")