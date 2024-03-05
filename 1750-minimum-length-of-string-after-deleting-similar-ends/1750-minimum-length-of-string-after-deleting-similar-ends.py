class Solution:
    def minimumLength(self, s: str) -> int:
        return self.delete_similar_ends(s, 0, len(s) - 1)

    # Deletes similar ends and returns remaining length
    def delete_similar_ends(self, s: str, begin: int, end: int) -> int:
        # The ends differ or meet in the middle
        if begin >= end or s[begin] != s[end]:
            return end - begin + 1
        else:
            c = s[begin]
            
            # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

            return self.delete_similar_ends(s, begin, end)