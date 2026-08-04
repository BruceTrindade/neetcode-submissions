class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        size = len(students)
        queue = deque(students)

        result = size

        for sandwiche in sandwiches:
            count = 0 
            while count < size and sandwiche != queue[0]:
                current = queue.popleft()
                queue.append(current)
                count += 1

            if sandwiche == queue[0]:
                result -= 1
                queue.popleft()
            else:
                break    

        return result            