class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        Set = set(arr)
        arr.sort()
        hashmap = {n: 1 for n in arr}
        for i in range(len(arr)):
            count = 0
            for j in range(0, i):
                a = arr[j]
                if arr[i] % a == 0:
                    b = arr[i] // arr[j]
                    if b in Set:
                        count += hashmap[a] * hashmap[b]
            hashmap[arr[i]] += count
        
        ans = sum(v for v in hashmap.values())
        return ans % (10 ** 9 + 7)
