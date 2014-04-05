# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

# with open("states.csv", "r") as states_file:
        # states = states_file.read().split("\n")

# print "<select>"

# for index, state in enumerate(states):
    # states[index] = states[index].split(",")
    # print "\t <option value='{0}'>{1}</option>".format(states[index][0], states[index][1])
# print "</select>"


# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

# with open("states.html","w") as states_html_file:
	# states_html_file.write("<select>")
	# for index, state in enumerate(states):
		# states[index]=states[index].split(",")
		# states_html_file.write("\t <option value='{0}'>{1}</option>".format(states[index][0], states[index][1]))
	# states_html_file.write("</select>")
	
# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.
with open("state-info.csv", "r") as states_info_file:
        states_info = states_info_file.read().split("\n")
		
with open("states_tables.html","w") as sti_html_file:
	for index, sti in enumerate(states_info):
		states_info[index]=states_info[index].split(",")
		sti_html_file.write("<table border='1' cellspacing='5'>")
		sti_html_file.write("<tr>")
		sti_html_file.write("<td colspan='2'><center><b><font FACE='Arial'> {0} </center></font></td></b>".format(states_info[index][1].replace('"', "")))
		sti_html_file.write("<tr>")
		sti_html_file.write("<tr>")
		sti_html_file.write("<td> <font FACE='Arial'>Rank: {0} </font></td>".format(states_info[index][0].replace('"','')))
		sti_html_file.write("<td> <font FACE='Arial'>Percent: {0} </font></td>".format(states_info[index][4].replace('"','')))
		sti_html_file.write("<tr>")
		sti_html_file.write("<tr>")
		sti_html_file.write("<td> <font FACE='Arial'>US House Members: {0}</font> </td>".format(states_info[index][3]))
		sti_html_file.write("<td> <font FACE='Arial'>Population: {0}</font> </td>".format(states_info[index][2]))
		sti_html_file.write("<tr>")
		sti_html_file.write("</table>")



# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.
