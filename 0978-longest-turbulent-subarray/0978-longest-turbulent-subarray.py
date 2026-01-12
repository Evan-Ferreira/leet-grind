class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr = 1
        res = 1
        for i in range(len(arr) - 1):
            if i > 0 and ((arr[i - 1] > arr[i] and arr[i] < arr[i + 1]) or 
                (arr[i - 1] < arr[i] and arr[i] > arr[i + 1])):
                curr += 1
            else:
                if arr[i] == arr[i + 1]:
                    curr = 1
                else:
                    curr = 2
            res = max(curr, res) 
        return res