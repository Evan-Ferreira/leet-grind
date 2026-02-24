class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        res = []
        replace = {}
        s = text.split("%")

        for key, val in replacements:
            replace[key] = val

        cache = {}

        def dfs(vals):
            if not vals:
                return ""

            if vals in cache:
                return cache[vals]
            tmp = ""
            for v in vals.split("%"):
                if v in replace:
                    tmp += dfs(replace[v])
                else:
                    tmp += v
            cache[vals] = tmp
            return tmp

        for k, v in replace.items():
            replace[k] = dfs(v)

        for r in range(2, len(text)):
            l = r - 2
            if text[l] == text[r] == "%" and text[l + 1] in replace:
                res.append(replace[text[l + 1:r]])
            elif text[l + 1] != '%':
                res.append(text[l + 1])
        return "".join(res)