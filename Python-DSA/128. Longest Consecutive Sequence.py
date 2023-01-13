class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seqs = collections.defaultdict(list)

        for i in nums_set:
            if i-1 in nums_set:
                continue

            num = i
            while num in nums_set:
                seqs[i].append(num)
                num = num + 1

        longest_len = 0
        for s in seqs.values():
            if len(s) > longest_len:
               longest_len =  len(s)

        return longest_len

             


            






        
                



            

        