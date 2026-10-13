class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # If total gas is less than total cost, completing the circuit is impossible
        if sum(gas) < sum(cost):
            return -1
        
        total_surplus = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            current_tank += net_gain
            
            # If we cannot reach station i + 1, reset candidate start to i + 1
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index