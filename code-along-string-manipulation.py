string1 = 'This is a valid string'
string2 = "This is also a valid string"
#string3 = "This is NOT valid - see why?"

palindrome = "Go hang a salami, I'm a lasagna hog." 

#Using the other quote for the nested quote
sting3 = "'Always look on the bright side of life,' he said."

#Using escaped quotes for the nested quote
string4 = "\"Always look on the bright side of life,\"he said."
#print(string4)

len(string4)
#print(len(string4))

#strip() function

name="     Erica   "
#print(len(name))
#print(name)

name_no_spaces = name.strip()
#print(len(name_no_spaces))
#print(name_no_spaces)

#split()

filepath = "/var/erica/here"
folders = filepath.split("/")
#print(folders)
#print(type(folders))

#join

windowsPath = "\\".join(folders)
#print(windowsPath)

reservation_name = "Froman, Abe"
char_to_find = ","

#Where is the comma?

char_location = reservation_name.find(char_to_find)
#print(char_location)

#index()
char_location = reservation_name.index(char_to_find)
#print(char_location)

#transformations

#print(reservation_name.upper())
#print(reservation_name.lower())
#print(reservation_name.title())
#print(reservation_name.swapcase())
#print(reservation_name.capitalize())

# f-strings

name = "Erica"
age = 33

#print(f"My name is {name} and I am {age}.")

a = 3
b = 9
#print(f'We can count to {b} by {a}: {a*2} {a*3}')

#replacing
name = "Eria Fatl"
name = name.replace("Eria", "Erica")
name = name.replace("Fatl", "Fatal")
print(name)