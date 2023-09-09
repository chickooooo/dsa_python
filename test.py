def solution_1(s: str) -> bool:
    count_list: list[int] = [0, 0, 0]

    for l in s:
        if l == '(':
            count_list[0] += 1
        elif l == ')' and count_list[0] == 0:
            return False
        elif l == ')':
            count_list[0] -= 1
        elif l == '[':
            count_list[1] += 1
        elif l == ']' and count_list[1] == 0:
            return False
        elif l == ']':
            count_list[1] -= 1
        elif l == '{':
            count_list[2] += 1
        elif l == '}' and count_list[2] == 0:
            return False
        elif l == '}':
            count_list[2] -= 1
    
    if count_list != [0, 0, 0]:
        return False

    return True


s = "()[]"
print(solution_1(s))

s = "(([])){}"
print(solution_1(s))

s = "(([[()]]))"
print(solution_1(s))

s = "((][()]]))"
print(solution_1(s))
