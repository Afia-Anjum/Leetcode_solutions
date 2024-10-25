# Example 2: You are given a binary string s (a string containing only "0" and "1").
# You may choose up to one "0" and flip it to a "1".
# What is the length of the longest substring achievable that contains only "1"?
# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.


s = "1101100111"
left=right=curr=0
answer=0
for right in range(len(s)):
    if s[right]=="0":
        curr+=1
    print("printing curr:")
    print(curr)
    while curr>1:
        if s[left]=="0":
            curr-=1
        left += 1
    print("printing right:")
    print(right)
    print("printing left:")
    print(left)
    print("printing individual length of valid subarrays:")
    print(right-left+1)
    answer=max(answer,right-left+1)
print("Printing final answer:")
print(answer)