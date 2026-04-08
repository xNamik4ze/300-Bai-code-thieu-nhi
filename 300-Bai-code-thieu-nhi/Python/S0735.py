class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for x in asteroids:
            while res and res[-1] > 0 and x < 0:
                dif = x + res[-1]
                if dif < 0:
                    res.pop()
                    continue
                elif dif == 0:
                    res.pop()
                    break
                else:
                    break
            else:
                res.append(x)
        return res