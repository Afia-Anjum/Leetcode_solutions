# class Solution:
#     def minStartValue(nums):
#         prefix=[nums[0]]
#         for i in range(1,len(nums)):
#             prefix.append(nums[i]+prefix[i-1])
#         start_value=min(prefix)
#         print(start_value)
#         print(prefix)
#         if start_value<0:
#             start_value=abs(start_value)
#         else:
#             start_value=1
#         while(1):
#             step_sum=start_value
#             flag=0
#             for i in range(len(nums)):
#                 step_sum=step_sum+nums[i]
#                 if step_sum<1:
#                     flag=1
#                     start_value+=1
#                     break
#             if flag==0:
#                 break
#         return start_value
#
#     print(minStartValue([5,6,7,8]))

#######Another way of doing it#########
# when you already know you don't have to think about the min start value when all values are positive, it will by default be 1.

class Solution:
    def minStartValue(nums):
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[i-1])
        start_value=min(prefix)
        if start_value>0:
            start_value=1
        else:
            start_value=1-start_value
        return start_value

    print(minStartValue([5,6,7,8]))