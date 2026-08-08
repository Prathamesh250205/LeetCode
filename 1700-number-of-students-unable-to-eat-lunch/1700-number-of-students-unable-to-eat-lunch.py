from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = Counter(students)
        for i, s in enumerate(sandwiches):
            if count[s] == 0:
                return len(sandwiches) - i
            count[s] -= 1
        return 0