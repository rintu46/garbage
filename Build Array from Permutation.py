class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            value_store = nums[nums[i]]
            # v =  nums[nums[i]]
            answer.append(value_store)
            print(value_store)
        return answer


 