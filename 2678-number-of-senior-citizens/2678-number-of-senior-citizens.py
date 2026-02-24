class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            age = d[11:13]
            if age[0] in ['6', '7', '8', '9'] and age != "60":
                res += 1
        return res