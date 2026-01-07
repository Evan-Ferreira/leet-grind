class Solution:
    def digitCount(self, num: str) -> bool:
        h = defaultdict(int)

        for dig in num:
            h[dig] += 1
        
        print(h)
        
        for i in range(len(num)):
            if h[str(i)] != int(num[i]):
                print(num[i], i)
                return False
        return True