import re
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = defaultdict(int)
        banned_set = set(banned)
        
        words = re.findall(r'\w+', paragraph.lower())
        
        for word in words:
            if word not in banned_set:
                counts[word] += 1

        return max(counts, key=counts.get)
