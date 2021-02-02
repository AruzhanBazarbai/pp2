class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        a=[]
        x=0
        a.append(x)

        for i in range(len(gain)):
            x+=int(gain[i])
            a.append(x)

        maxi=-101

        for i in range(len(a)):
            if maxi<a[i]:
                maxi=a[i]
        return(maxi)
