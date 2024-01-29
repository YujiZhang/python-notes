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
    
# output
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
    
# output
# i = 0 , list is [1, 2, 3, 4, 5]
# i = 1 , list is [1, 2, 3, 4]
# i = 2 , list is [1, 2, 3]
# i = 3 , list is [1, 2]
# i = 4 , list is [1]    