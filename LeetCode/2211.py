

class Solution:
    def countCollisions(self, directions: str) -> int:
        cnt = 0
        acum = 0
        road = []
        for direction in directions:
            if road and road[-1] == 'S' and direction == 'L':
                cnt += 1
            elif road and road[-1] == 'R' and direction == 'L':
                road.append('S')
                cnt += acum + 1
                acum = 0
            elif road and road[-1] == 'R' and direction == 'S':
                cnt += acum
                acum = 0
                road.append('S')
            elif direction != 'L':
                if direction == 'R':
                    acum += 1
                road.append(direction)

        return cnt