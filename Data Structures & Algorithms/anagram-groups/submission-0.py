from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        base = ord('a')
        result = defaultdict(list)
        for s in strs:
            hash = [0] * 26
            for char in s:
                hash[ord(char) - base] += 1
            
            result[tuple(hash)].append(s)
        
        return list(result.values())


        '''
        # create hashmap for the number of letters
        results = []
        len_grps = defaultdict(list)
        for i in range(len(strs)):
            len_grps[len(strs[i])].append(strs[i])
        for i in range(len(len_grps.keys())):
            if len(len_grps[i]) == 1:
                results.append(len_grps[i])

        match_count = 0
        for j in range(len(strs)):
            char_count = [0] * 26
            if match_count == 0:
                pass
        
        base = ord('a')
        results = []

        hash_list = [] * len(strs)
        for i in range(len(strs)):
            hash = [0] * 26
            for char in strs[i]:
                hash[ord(char) - base] += 1
            hash_list.append(hash)
        
        #size_hash = {}
        #for j in range(len(hash_list)):
        #    size_hash[len(hash_list[j])].append(j)
        result_hash = defaultdict(list)
        for j in range(len(hash_list)):
            for k in range(len(hash_list)):
                
                #if len(hash_list[j]) != hash_list[k]:
                    #continue
                
                if hash_list[j] == hash_list[k]:
                    result_hash[j].append(strs[j])
                    result_hash[j].append(strs[k])
                    del(hash_list[k])

        
        print(result_hash)
        '''



