# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = set()
#         n, p, z = [], [], []
#         i = j  = 0
#         for num in nums:
#             if num > 0:
#                 p.append(num)
#             elif num < 0:
#                 n.append(num)
#             else :
#                 z.append(num)
        
#         N, P = set(n), set(p)

#         if len(z)>= 3:
#             result.add((0,0,0))  # 3 or more zero's are there
        
#         if z:
#             for num in p:
#                 if -1*num in n:
#                     result.add((-1*num, 0, num))   # one zero and other two numbers
        
#         for i in range(len(n)):
#             for j in range(i+1,len(n)):
#                 target = -1*(n[i]+n[j])
#                 if target in p:
#                     result.add(tuple(sorted([n[i], n[j], target])))   # two negative and one positive
        
#         for i in range(len(p)):
#             for j in range(i+1, len(p)):
#                 target = -1*(p[i]+p[j])
#                 if target in n:
#                     result.add(tuple(sorted([p[i], p[j], target])))
        
#         return result

# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         res = set()
#         n = len(nums)

#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 x = -(nums[i] + nums[j])

#                 if x in nums[j + 1:]:
#                     res.add((nums[i], nums[j], x))

#         return [list(t) for t in res]
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

        
