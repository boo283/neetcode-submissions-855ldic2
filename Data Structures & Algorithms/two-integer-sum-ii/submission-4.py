class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1
        while(True):
            sum=numbers[head] + numbers[tail]
            if target < sum:
                tail -= 1
            elif target > sum:
                head += 1
            else:
                return [head+1, tail+1]

        
        

        