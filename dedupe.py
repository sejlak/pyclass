# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.
# Goal 2: Who came to *both* your Film Screening and your Happy hour?

def dedupe_text(filename1, filename2):

    """ 
        
    """
    with open(filename1,"r") as text_file1:
        text1=text_file1.read().split("\n")
    with open(filename2,"r") as text_file2:
        text2=text_file2.read().split("\n")
        
    all_emails = text1+text2
        
    from_list = list(set(all_emails))

    return from_list

deduped_list= dedupe_text("film_screening_attendees.txt","happy_hour_attendees.txt")

for index, email in enumerate(deduped_list):
    deduped_list[index] = deduped_list[index].split(",")

    print "{0} came to both events!".format(deduped_list[index][0])   



