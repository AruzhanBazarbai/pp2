class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=""

        for x in address:
            if x=='.':
                res+='[.]'
            else:
                res+=x
        return(res)
        