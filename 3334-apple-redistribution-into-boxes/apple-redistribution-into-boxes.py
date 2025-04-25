class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        num_boxes = 0

        capacity.sort(reverse = True)

        for cap in capacity:
            total_apples -= cap
            num_boxes += 1
            if total_apples <= 0:
                break
        
        return num_boxes