# if statement loops through once
# while statement does it as long as it's true

#LESSON 3: FILE HANDLING
#file handling lets Python read and write to files
##Read from and write to spreadsheet
##Read from and write to text file

# EXAMPLE 1:
# with open("states.txt","r") as states_file:
	# states=states_file.read()
	# print states 
	
# EXAMPLE 1 EXPLANATIONS:	
# with keyword: similar to conditional by having an indentation level for code below. 
# Whatever is indented, we will be doing that "with" the file that we're opening.
# Don't have to worry about closing the file once you're done with your indented commands. 

# open() built-in function, tells Python to open a file. 
# The way we tell Python which file to open, we specify an argument inside the parentheses. 
# Notice that the file you open is a string. 

# Relative paths are the pathway to your file you want to open relative to where the script you're running lives. 
# If you have your scripts in... C:/Users/Sejla/Desktop/pyclass
# Python will look for your file in the same folder.

# Argument 2: The "mode" to open the file in, as a string
	# r: read-only--just read this file, don't do anything to it. 
	# w: write mode--create this file if it doesn't exist, and write to it. If it does exist, write over it. 
	# a: append mode--If your file exist, it'll just add the info to the end of your old file. (friendly, doesn't erase old work) 
	
# The as keyword is used to create a variable out of your file handler. The variable in this example is states_file, but you can use any 
# variable name. 

# .read() is a file method--a function that only works with file handlers. The file handler is states_file. 
# .read() will take the entire contents in a file and turn them into a string and store them in states. 

#try (make sure this text file is saved in the same folder as your .txt file and run it as a script)
with open("states.txt","r") as states_file:
	states=states_file.read()
	print states 
	
#.read() gives us the file contents as a string. If we have a string, we can turn it into a list!
# add the following line to the end of your second line as follows:
# states=states_file.read().split("\n")
# splits the string into a list and splits it into a new line, so every state and its abbreviation are on the same line.
# it will print out a \t between the abbreviation and state name to indicate that there's a TAB there. 

# this is the same as running above code with a second line (which doesn't have to be indented):
# states=states.split("\n")


with open("states.txt","r") as states_file:
	states=states_file.read().split("\n")
	print states 
	
#LET'S TRY IT OUT: CSV FILES
#We're splitting the file into a list at each line, adn then individually splitting each line into a list by the commas. 
with open("states.csv", "r") as states_file:        
    states = states_file.read().split("\n")

#enumerate wraps around the list and gives you the slicing number and the value itself. e.g., [1] AL,Alabama...[4]AR,Arkansas
for index, state in enumerate(states):
    states[index] = states[index].split(",")

    print "{0}'s abbreviation is {1}".format(states[index][1], states[index][0])   
	
#Dictionaries: WHY
# Create a list of names and Github names for each student in the class
# If we wanted to look up a specific person's Github name, how could we do that? 

#Dictionaries have two components: a key and its corresponding value. 
#Creating an empty Dictionary. 
contacts={}

#Creating a dictionary with items in it:
contacts={'Shannon': '202-555-1234',
'Bridgit':'703-555-9876',
'Christine':'410-555-7777'
}

# reading part of a string (example from class 2)
# print name[0,5] #Shannon
# Reading part of a list
# print attendees[:3] #Amy,Jen,Julie

#Reading part of a dictionary:
print contacts['Shannon'] #202-555-1234 

#Adding to a dictionary:
contacts['Mel']='301-333-1212'

#Reading from a dictionary(error prone)
#print contacts['Frankenstein']

#reading from a dictionary (no errors)
#use "get" so your program doesn't crash
print contacts.get('Frankenstein') #none

#Dictionaries can also contain strings, lists, or other dictionaries 
#phonebook['Mel'] = '301-333-1212'

attendees = {
'Feb 1': ['Jen', 'Amy'],
'Feb 2': ['Rachel', 'Aliya']
}

#order does not matter, because you have the key (e.g., 'phone' and 'twitter')
contacts = {
'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },
'Anupama': {'phone': '410-333-9876','twitter': '@iamtheanupama', 'github': '@apillalamarri'}
}

#keys are picky and case-sensitive, they're always strings, etc. 
print contacts['Shannon']
print contacts['Shannon']['github']

#Looping through dictionaries 
#Looping through by keys
#.keys() creates a list of the keys of that dictionary, which you can then loop over.
for contact in sorted(contacts.keys()):#dictionary method .keys, only works on dictionaries, and sorted() sorts it alphabetically
	print contact #notice that Anupama is second, python will never preserve the order of your dictionaries 
	print contacts[contact] #this gives you all the values of in the additional dictionary of contacts 

#Looping through dictionary by values if the keys don't matter to us--if all you need is the info in the values of the dictionaries 
#For example, if all you wanted to do was see how common 202 numbers are
#.values() is much less useful and common 
for contact_info in contacts.values():
	print contact_info 

#.items() creates a nested list of the key and values of that dictionary which you can then loop over. 	
for contact, info in contacts.items(): 
	print contact, info 
	
# EXERCISE: Loop through that dictionary to display everyone's contact information, like this:
# Shannon's contact information is:
	# Phone: 202-555-1234
	# Twitter: @svt827
	# Github: @shannonturner


for contact in sorted(contacts.keys()):
	print "\n"
	print "{0}'s information is:".format(contact)
	print "  Phone:{0}".format(contacts[contact]['phone']) 
	print "  Twitter:{0}".format(contacts[contact] ['twitter'])
	print "  Github:{0}".format(contacts[contact]['github'])
	print "\n"
	



