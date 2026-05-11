class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1


        freqs = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():

            freqs[freq].append(num)

        res = []


        for i in range(len(freqs) - 1, -1, -1):
            if freqs[i]:
                for num in freqs[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
