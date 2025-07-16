#play with for loops

#create a list

erica_list = []
print("My todo list:", erica_list)

erica_list.append("clean the bathroom")
erica_list.append("sign up for dance class")
erica_list.append("Call sister")
erica_list.append("get nails done")

print("List:", erica_list)

#use a for loop to iterate through the list

erica_list.insert(1, "pay credit card bill")
print(erica_list)


print("First task:", erica_list[0])
print("Last two tasks:", erica_list[-2:])


done_task = erica_list.pop(2)
print("I completed:", done_task)
print("To-do list after removal:", erica_list)


#print a task list

print("Here's what I still need to do:")
for task in erica_list:
    print("-", task)