#Given an integer array nums, find all the unique numbers x in nums
# that satisfy the following: x + 1 is not in nums, and x - 1 is not
# in nums.

def find_unique_numbers_of_x_with_a_constraint(nums):
    dict={}
    answer=[]
    for i in range(len(nums)):
        dict[nums[i]]=i
    for key in dict.keys():
        if key+1 in dict.keys() or key-1 in dict.keys():
            continue
        else:
            answer.append(key)
    return answer

print(find_unique_numbers_of_x_with_a_constraint([6,2,0,5,11]))


#with if....not...


# def find_unique_numbers_of_x_with_a_constraint(nums):
#     dict={}
#     answer=[]
#     for i in range(len(nums)):
#         dict[nums[i]]=i
#     for key in dict.keys():
#         if (key+1 not in dict.keys()) and (key-1 not in dict.keys()):
#             answer.append(key)
#     return answer
#
# print(find_unique_numbers_of_x_with_a_constraint([6,2,0,5,11]))



# #With set
# def find_numbers(nums):
#     ans = []
#     nums = set(nums)
#
#     for num in nums:
#         if (num + 1 not in nums) and (num - 1 not in nums):
#             ans.append(num)
#
#     return ans
#
# print(find_numbers([6,2,0,5,11]))