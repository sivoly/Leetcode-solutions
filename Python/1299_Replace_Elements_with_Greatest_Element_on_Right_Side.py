class Solution(object):
    def replaceElements(self, arr):
        max1=-1
        n=len(arr)
        for i in range(n-1,-1,-1):
            current=arr[i]
            arr[i]=max1
            max1=max(max1, current)
        return arr
        
