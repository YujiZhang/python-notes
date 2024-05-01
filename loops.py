# -*- coding: utf-8 -*-

'''
in while loop, the while condition is re-evaluated at each iteration
loop length can be adjusted dynamically (eg below by altering `nums`) 
'''
nums = [1,2,3,4,5]
i = 0

while i <= len(nums)-1:

    print('i =', i, ', element =', nums[i], 'in list', nums)
    i += 1    
    del nums[-1]
    
# i = 0 , element = 1 in list [1, 2, 3, 4, 5]
# i = 1 , element = 2 in list [1, 2, 3, 4]
# i = 2 , element = 3 in list [1, 2, 3]




'''
in for loop, the i sequence is generated at the beginning
here changing `nums` does not impact the i sequence or the loop
''' 
nums = [1,2,3,4,5]

for i in range(len(nums)):

    print('i =', i, ', list is', nums)    
    del nums[-1]
    
# i = 0 , list is [1, 2, 3, 4, 5]
# i = 1 , list is [1, 2, 3, 4]
# i = 2 , list is [1, 2, 3]
# i = 3 , list is [1, 2]
# i = 4 , list is [1]    

'''
but for-enumerate is evaluated at each iteration!
'''
nums = [1,2,3,4,5]

for i, item in enumerate(nums):

    print('i =', i, ', list is', nums)    
    del nums[-1]
    
# i = 0 , list is [1, 2, 3, 4, 5]
# i = 1 , list is [1, 2, 3, 4]
# i = 2 , list is [1, 2, 3]








'''
use emuerate to loop through indeces and elements

'''


letters = list('abcd')

# don't use this - less readable
for index in range(len(letters)):
    print(index, letters[index])
    
# 0 a
# 1 b
# 2 c
# 3 d    
    
# this is neater and more pythonic
for index, item in enumerate(letters):
    print(index, item)

# 0 a
# 1 b
# 2 c
# 3 d


#### loop but skipping last element 
for index, item in enumerate(letters[:-1]):
    print(index, item)

# 0 a
# 1 b
# 2 c


#### loop but skipping first element 

# this doesn't work: 
# because letters[1:] = ['b', 'c', 'd'], so index is messed up
for index, item in enumerate(letters[1:]):    
    print(index, item)
    
# 0 b
# 1 c
# 2 d

# I feel this way easiest, although it's more lines of code
for index, item in enumerate(letters):
    
    if index <= 0:
        continue
    
    print(index, item)

# 1 b
# 2 c
# 3 d

#### loop backwards
for index, item in reversed(list(enumerate(letters))):
    print(index, item)
    
# 3 d
# 2 c
# 1 b
# 0 a