'''
Dandel Oliver S. Prado
2025-01061
CMSC 12 G-6L
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def studentRegis():
	student_names = [] #list to store student names to be inputted by the user
	userinput = int(input("How many students will be registered?: ")) 

	for i in range(userinput): 
		full_name = input(f"Enter full name of student #{i+1}: ") #prompts user for full name of student #n
		student_names.append(full_name)

	print(f"\nTotal student:", len(student_names))
	print(f"List of students:{student_names}")

	first_names = [] #splits the names of students from the var student_names and stores it in this list
	for name in student_names:
		x_first_name = name.split()[0] 
		first_names.append(x_first_name)
	print("First Names: ", first_names)

	student_names.sort() #sorts the names alphabetically
	print(f"\nSorted students: {student_names}")

	longest_name = "" #longest name is currently an empty string 
	for name in student_names:
		if len(name) > len(longest_name):
			longest_name = name 
			#if the new name is longer than the empty string/current longest name, it becomes the new longest name 
	print(f"Student with the longest name: {longest_name}")

	name_search = input("\nSearch for a student: ") #prompts user to search for a student
	if name_search in student_names: 
		index = student_names.index(name_search)
		print(f"{name_search} is found at index {index}")
	else:
		print("Student not found") #if user tries to search for a student that DNE in the list
	
studentRegis()
