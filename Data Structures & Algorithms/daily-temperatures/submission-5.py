class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        
        currentTemps = []
        for i in range(0, len(temperatures)):
            index = i-1
            while currentTemps and currentTemps[len(currentTemps)-1] < temperatures[i]:
                if answer[index] != 0:
                    index -= 1
                    continue
                answer[index] = i-index
                index -= 1
                currentTemps.pop()

            currentTemps.append(temperatures[i])

        return answer
