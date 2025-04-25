class Solution:
    def clearDigits(self, s: str) -> str:
        ls = list(s)
        for i in range(len(ls)):
            if ls[i].isdigit():
                ls[i] = ""
                for j in range(i, -1, -1):
                    if ls[j] != "":
                        ls[j] = ""
                        break
        return "".join(ls)