# LIST AND DICTIONARY COMPREHENSIONS

## <PROJECT: NATO PHONETIC ALPHABET>
Prompt user to enter a word.
return a list of the corresponding nato phonetic alphabet characters

## list comprehension
a list comprehension is creating a new list from a previous list
    
    new_list = [new_item for item in list]
^template^ keywords: new_item, item, list

    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        add_1 = n+1
        new_list.append(add_1)
becomes

    numbers = [1, 2, 3]
    new_list = [n+1 for n in numbers]
list comprehensions work with any iterable
    name = "Angela"
    new_list = [letter for letter in name]
iterable with an order is a 
# sequence
## list, string, tuple, range

    list = [n*2 for n in range(1,5]

conditional LC's
    new_list = [new_item for item in list if condition]
    
    names = ["alex", "beth", "caroline", "dave", "Eleanor", "Freddie"]

# dict comprehension
## new_dict = {new_key:new_value for item in list}
^assumes item is already a (k,v) tuple
item can be the key or the value, and a function can be used for the other
## new_dict = {new_key:new_value for (key, value) in dict.items()

kinda of like pandas version of enumerate():

    for (index, row) in student_df.iterrows():
    print(index)
    print(row)

    student_dict = {
        "student": ["Angela", "James", "Lily"], 
        "score": [56, 76, 98]
    }
    
    #Looping through dictionaries:
    for (key, value) in student_dict.items():
        #Access key and value
        pass
    
    import pandas
    student_data_frame = pandas.DataFrame(student_dict)
    
    #Loop through rows of a data frame
    for (index, row) in student_data_frame.iterrows():
        #Access index and row
        #Access row.student or row.score
        pass
    
    # Keyword Method with iterrows()
    # {new_key:new_value for (index, row) in df.iterrows()}
