class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for r in range(k - 1, len(arr) - 1):
            if (abs(arr[r - k + 1] - x) > abs(arr[r + 1] - x) or
                arr[r - k + 1] == arr[r + 1]):
                continue
            return arr[r - k + 1: r + 1]
        return arr[len(arr) - k:]