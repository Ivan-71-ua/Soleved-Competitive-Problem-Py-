
class Solution:
    def countCollisions(self, directions: str) -> int:
        cnt = 0
        road = []
        for direction in directions:
            if road and road[-1] == "R" and direction == "L":
                cnt += 2
                road.append(direction)
            if road and road[-1] == "S" and direction == "L":
                road.append(direction)
                cnt += 1
            if direction != "L":
                road.append(direction)

        return cnt