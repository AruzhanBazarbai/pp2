class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       
        cnt=0
        
        for i in range (len(nums)):
            b=nums[i]
            x=i
            for j in range (x+1,len(nums)):
                if b==nums[j] and x<j:
                    cnt+=1

        return(cnt)
   

