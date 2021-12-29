# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.searchBadVersion(n, 0, n)

    def searchBadVersion(self, n, start, stop):
        index = (start+stop)//2
        if isBadVersion(index):
            if start >= stop:
                return index
            return self.searchBadVersion(n, start, index-1)
        else:
            if start >= stop:
                return index+1
            return self.searchBadVersion(n, index+1, stop)
