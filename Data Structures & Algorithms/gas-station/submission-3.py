class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        amount = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            amount += g - c
            if amount < 0:
                amount = 0
                start = i + 1
        return start 
            