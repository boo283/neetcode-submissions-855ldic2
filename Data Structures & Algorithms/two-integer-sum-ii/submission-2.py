class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1
        while(True):
            if target < numbers[head] + numbers[tail]:
                tail -= 1
            elif target > numbers[head] + numbers[tail]:
                head += 1
            else:
                return [head+1, tail+1]

        
        

        