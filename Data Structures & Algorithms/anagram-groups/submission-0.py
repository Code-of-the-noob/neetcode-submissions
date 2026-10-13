class Solution:
    def stringify_counter(self, counter):
        result=""
        for key in sorted(counter.keys()):
            result+=key+str(counter[key])
        return result


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage=defaultdict(list)
        for word in strs:
            storage[self.stringify_counter(Counter(word))].append(word)

        print(storage)

        result=[]
        for key,val in storage.items():
            result.append(val)

        return result