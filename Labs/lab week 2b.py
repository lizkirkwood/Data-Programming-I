#Liz Kirkwood
#Unless otherwise noted, try solving these using class content and without searching online

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i < 5:
        print('little')
    elif i == 5:
        i += 1
        continue
    elif i > 5:
        print('big')
    else:
        print('what happened?')
    print('Finished!')
    i += 1

#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4



for i in range(1,4):
    print(i,(i+1))

        



#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list

start_list = [[2, 3, 4], [6, 8, 9]]
newlist = []   #https://stackoverflow.com/questions/18072759/how-can-i-use-list-comprehensions-to-process-a-nested-list
for sub_list in start_list:
    for i in sub_list:
        if i % 2 == 0:
            newlist.append(int(i/2))
print(newlist)


start_list = [[2, 3, 4], [6, 8, 9]]
flat_list = [i for sub_list in start_list for i in sub_list ]    
#Source: https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
final_list = [(int(i/2)) for i in flat_list if (i %2 == 0)]
print(final_list)



#4
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end

new_dict = {key.capitalize():datetime.datetime.strptime(val, "%m/%d/%Y") for key, val in start_dict.items()}
#Source: https://stackoverflow.com/questions/9504356/convert-string-into-date-type-on-python
print(new_dict)
    