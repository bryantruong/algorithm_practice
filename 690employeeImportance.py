# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id: int) -> int:
        # First, generate the dictionary that allows us to map ID to employee information
        # O(N), where N is the number of employees
        employee_dict = {}
        for employee in employees:
            employee_dict[employee.id] = employee
        return self.recursiveGetImportance(employee_dict, id, 0)

    def recursiveGetImportance(self, employee_dict, id, current_sum):
        # Time complexity worst case would be O(N), since worst case, we are querying the head honcho.
        employee_info = employee_dict[id]
        current_sum += employee_info.importance
        if not employee_info.subordinates:
            return current_sum
        # Recursively add up each subordinate's importance
        for subordinateID in employee_info.subordinates:
            current_sum = self.recursiveGetImportance(employee_dict, subordinateID, current_sum)
        return current_sum

def listToEmployees(listInput):
    employeesList = []
    for listItem in listInput:
        employeesList.append(Employee(listItem[0], listItem[1], listItem[2]))
    return employeesList

if __name__ == '__main__':
    employee_list = listToEmployees([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]])
    solutionObject = Solution()
    solutionObject.getImportance(employee_list, 1)