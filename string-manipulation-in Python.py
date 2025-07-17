to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglass Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
#print(changed_values)

lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split("\n")
print(lyrics_split)

lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
changed_values = lyrics.splitlines()
#print(changed_values)

long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = long_village_name
#print(len(string_length))

my_path = '   /c/Users/instructor/Downloads/Submit Relating the NonrelationalAssessment Download May 10, 2021 917 AM      '
my_folders = my_path.strip().split("/")
print(my_folders)

composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
# Separate the composers
composers = composers.replace('Mozart,Wolfgang', 'Wolfgang Mozart')
print(composers)

composers_split = composers.split(";")
print(composers_split)

# Get the third composer
third_composer = composers_split[2]
print(third_composer)


# Find the comma in the name
comma_position = third_composer.find(",")
print(comma_position)


# Use the slicing notation to get the last name
#ast_name = third_composer[]


# Use the slicing notation to get the first name
#irst_name = third_composer[]


# Join the names to get the 3rd composer's name in "first last" format
first_name = "Wolfgang"
last_name = "Mozart"
full_name = first_name + last_name
print(f"{first_name} {last_name}")
print(full_name)

left_padded = ' Operators are standing by'
right_padded = 'Call now '
clean_strings = right_padded.strip() + '!' + left_padded.strip("'")
print(clean_strings)

student_name = "Owen"
grade = 94.75
assignment_number = 12
print()

#Given the employee ID of "30", pad the string with zeroes on the left to have the employee ID appear as 6-digits "000030"
employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print(employee_id_padded)

#Print the following statement using raw strings:
print(r"\n/ represents a new line.\n/")

#Convert the following strings based on their variable names.
i_want_to_yell = 'yeah'
I_NEED_TO_BE_QUIET = 'SHHHHH'
this_is_a_title = 'this is a title'
sWAPcASE = 'sWAPcASE'
capitalize_this = 'capitalize this'
#Use print and a function to achieve what the variable names suggest.

print(i_want_to_yell.upper())
print(I_NEED_TO_BE_QUIET.lower())
print(this_is_a_title.title())
print(sWAPcASE.swapcase())
print(capitalize_this.capitalize())
