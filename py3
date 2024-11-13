class Solution:
    def countFairPairs(self, a: List[int], l: int, u: int) -> int:
        return a.sort() or sum(bisect_right(a,u-v,i+1)-bisect_left(a,l-v,i+1) for i,v in enumerate(a))
