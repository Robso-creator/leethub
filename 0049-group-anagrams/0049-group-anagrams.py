class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wrd_hash = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a - z on count

            for l in s:
                count[ord(l) - ord("a")] += 1 # if a ord value == 80 and  l== a then 80-80=0

            wrd_hash[tuple(count)].append(s)

        return list(wrd_hash.values())

        # S and T: O(m*n) m qtd of str on strs and n avg size of the anagrams