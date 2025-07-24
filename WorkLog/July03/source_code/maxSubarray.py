def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) <= 1:
        return (sum(nums))
    m = nums[0]
    s = nums
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if sum(s[i:j]) > m:
                m = sum(s[i:j])
    return (m)
