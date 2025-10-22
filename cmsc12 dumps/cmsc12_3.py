def palindrome(list): #will only work assuming that the words will not have spaces or " " between them
    t_value = []
    for word in list:
        no_space = word.replace(" ", "") #this line was added to make sure it follows the problem
        new_word = no_space[::-1] # reverse of a string is [::-1]
        if new_word == no_space: #comparison, palindrome checker
            t_value.append(True) #returns the bool value in the list
        else:
            t_value.append(False)
    return t_value
    
#test
list_1 = ["madam", "race car"] #result should be true, true
results = palindrome(list_1)
print(results)

