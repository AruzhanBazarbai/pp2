class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        pr=1
        sum=0
        while n>0:
            y=n%10
            pr*=y
            sum+=y
            n//=10
        return(pr-sum)
    