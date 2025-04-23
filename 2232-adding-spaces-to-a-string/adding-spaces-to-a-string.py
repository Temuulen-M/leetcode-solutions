class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ''
        space_idx = 0
        for idx in range(len(s)):
            if space_idx<len(spaces) and idx == spaces[space_idx]:
                output += ' '
                space_idx += 1
            output += s[idx]
            idx+=1
        return output