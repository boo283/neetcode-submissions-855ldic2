class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1
        while(True):
            sum=numbers[head] + numbers[tail]
            if sum==target:
                return [head+1, tail+1]
            elif target < sum:
                tail -= 1
            else:
                head += 1
        
        

        