class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = [m.start(0) for m in re.finditer(needle, haystack)]
        if res != []:
            return res[0]
        return -1