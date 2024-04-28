if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_student = {name: score}
        students.update(new_student)
    values = list(students.values())
    first = min(values)
    second = max(values)
    for i in range(len(values)):
        if first < values[i] < second:
            second = values[i]
        elif values[i] < first:
            second = first
            first = values[i]
    names = [name for name in students if students[name] == second]
    for name in sorted(names):
        print(name)