class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        saw_dict_t = {}
        saw_dict_s = {}
        
        if len(s) != len(t):
            return False

        for wrd_s in s:
            if wrd_s not in saw_dict_s:
                saw_dict_s[wrd_s] = 1
            else:
                saw_dict_s[wrd_s] += 1


        for wrd_t in t:
            if wrd_t not in saw_dict_t:
                saw_dict_t[wrd_t] = 1
            else:
                saw_dict_t[wrd_t] += 1

        for k, v in saw_dict_s.items():
            if k not in saw_dict_t or saw_dict_t[k] != v:
                return False

        return True

        #S: O(N)
        #T: O(N)