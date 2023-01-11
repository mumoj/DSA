class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre_product = 1
        for n in nums:
            pre_product = pre_product * n
            prefix.append(pre_product) 

        postfix = []
        post_product = 1
        for i in range(len(nums)-1,-1,-1):
            print(i)
            post_product = post_product  * nums[i]
            postfix.append(post_product)

        res = []
        postfix.reverse()
        for i in range(len(nums)):
            product = None
            if i == 0:
                product = 1 * postfix[i+1]
            elif i == len(nums)-1:
                product = prefix[i-1] * 1
            else:
                product = prefix[i-1] * postfix[i+1]
            res.append(product)

        return res





























        
