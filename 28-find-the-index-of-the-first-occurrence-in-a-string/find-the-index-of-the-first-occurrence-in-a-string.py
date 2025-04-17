class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(re.escape(needle), haystack)
        return match.start() if match else -1