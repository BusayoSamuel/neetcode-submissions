class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = list(zip(position, speed))
        pos_and_speed.sort(key=lambda x:x[0], reverse=True)

        stack = []

        for pos, speed in pos_and_speed:
            time = (target - pos)/speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        
        