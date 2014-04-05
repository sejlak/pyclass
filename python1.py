x="""
Hello! She said, "This matters, I promise," because I said so. Don't worry about it.
"""
z="""
Double quotes don't have issue "with" other double quotes "yay" she'said
"""

output="""
Event Name \t \t Date\Time
Happy Hour \t \t 7/21, 6:00 pm
Jane's House Party \t 7/22, 8:00 pm
"""

#use slicing to print out the middle 3 numbers
phone = "(123) 456-7890"
print phone[6:9]

phone="13306088444"
print "Local: {0}-{1}".format(phone[4:7],phone[7:])
print "Domestic: ({0}) {1}-{2}".format(phone[1:4],phone[4:7],phone[7:])
print "International: +{0}-{1}-{2}-{3}".format(phone[0],phone[1:4],phone[4:7],phone[7:])

#similar to ctrl+f
email_address="sejlakaralic@gmail.com"
email_address.find("@")

#similar to ctrl+h
phone = "555-1245"
phone.replace("1245","1234")

#find the length of your string
len(phone)

string2="Pie %%%%%%%%%%%"
print string2.strip("%")

#nesting functions if you want to count all "l's" not just a certain case
string3="allcaps"
print string3.upper().count("L")

#Conditionals
age=20

if age >= 21:
	print "I'll have a Three Philosophers"
elif 21> age>=18:
	print "I'm old enough to vote, but not enough to drink."
else:
	print "Why am I in this bar?"
	
# ###Create a quick calculator program that asks the 
# user for their recruitment goal and their current 
# recruitment numbers. The program should tell the 
# user whether they are at, below, or above their 
# goal.###

recruitment_goal=126
current_recruitment=95
if current_recruitment<=126:
	print "You're below your goal by {0}, keep working!".format(recruitment_goal-current_recruitment)

# if times_volunteered >= 5 or 
# (volunteer_type == 'Phone 
# Banking' and 'fundraising' in 
# volunteer_skills):
# have them ask supporters for money

times_volunteered=8
volunteer_type="Phone banking"
volunteer_skills="fundraising"

#Using string methods with conditionals
volunteer_type="Canvasser"
volunteer_name="SeJLa"

if volunteer_type.lower() =="canvasser" and volunteer_name.lower()=="sejla":
	print "great success"

#Lists are created by placing items in []
attendees=["Shannon","Jenn","Grace"]

print attendees[0] #this will return Shannon from your list
print attendees[0:] #this will print the entire list
print attendees[0:1] #this will print the first two values

#you can also find the length of your list
print len(attendees)
#or reassign a variable to  give you the length of your list
no_of_attendees=len(attendees)
print no_of_attendees

#appending things to lists
attendees_ages=[]
attendees_ages.append(28)
#to append multiple items, use extend() 
attendees_ages.extend([27,25])
print attendees_ages

#replacing items in lists
attendees_ages[0]=29

#deleting items, but pop can also be used as something else
day=days_of_week.pop()
print day
day=days_of_week.pop(3)

#You're on slide 17
