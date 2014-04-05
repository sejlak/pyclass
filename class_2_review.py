#lists are created by placing items inside of []
#you can create an empty list like so:
attendees=[]
#items in lists are separated by commas
attendees=["Sejla", "Randall","Albert", "Orit","Shane", "Amy", "Howard"]
#list slicing, to print parts of lists
print attendees[:2]#Sejla and Randall
print attendees[2:]#Albert,Orit,Shane,Amy,Howard
print attendees[2]#Albert
#You can find the length of a list by using the len() command
print len(attendees)#7
#you can even save that in a variable
number_of_attendees=len(attendees)
#adding items to a list--list.append() adds an item to the end 
attendees_ages=[]
attendees_ages.append(27)
print attendees_ages 
#to change existing items in the list, you must specify what position it is 
attendees_ages[0]=28
print attendees_ages #28
#Quick Exercise, append the rest of the days of the week
#Note, you cannot append two items at a time using .append()
days_of_week = ['Monday', 'Tuesday']
days_of_week.append('Wednesday') 
days_of_week.append("Thursday")
days_of_week.append("Friday")
days_of_week.append("Saturday")
days_of_week.append("Sunday")
print len(days_of_week) #7
#deleting items from lists using .pop()
print days_of_week
day=days_of_week.pop()
print day #sunday, because .pop() removed sunday
print days_of_week #no more sunday in list
day=days_of_week.pop(3) #removes Thursday from days_of_week list and saves it as day
#Remember how .append() could only add one item to a list?
#Well, .extend() can add multiple items, below is some code that does just that 
months=["January","February"]
months.extend(["March","April","May","June","July","August","September","October","November","December"])
#remove the first month in the list
months.pop(0)
#Insert January before index 0
months.insert(0,"January")
#transform a string into a list
address="2021 Key Blvd. Arlington, VA 22201"
address_as_list=address.split(" ")#In this case, if Python sees a space, it will split the string at that marker, but you can use anything.
#The "in" keyword allows you to check whether a value exists in the list
#Also works with strings!
"ann" in "Shannon" #true
"Frankenstein" in python_class
#Use raw input to have people input their addresses
address=raw_input("Enter your address here: ")
address_list=[]
address_list.append(address)
print address_list
#Ranges of numbers
range(5) # [0, 1, 2, 3, 4] 
# range(start, stop)
range(5,10) # [5, 6, 7, 8, 9]
for number in range(10):
	print number
#LOOPS: for loop exercise
#change quadrant code to use for loop instead of repeating the code three times
quadrant=[]
for address in range(3):
	address=raw_input("Enter your address here: ")
	if "NW" or "NE" or "SE" or "SW" in address:
		quadrant.append(address)
	print quadrant
	
#YOU'RE ON SLIDE 24


