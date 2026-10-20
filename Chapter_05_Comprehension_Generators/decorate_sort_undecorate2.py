# Resolve conflict when the total grade is the same
students = [
        dict(id=0, credits=dict(math=9, physics=6, history=7)),
        dict(id=1, credits=dict(mth=6, physics=7, latin=10)),
        dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
        dict(id=3, credits=dict(math=5, physics=5, geography=7)),
        dict(id=4, credits=dict(history=8, physics=9, chemistry=10))
        ]

def decorate(student):
    # create a 2-tuple (sum of credits, student) from the dictionary
    # Introduce ID as well for sorting
    return sum(student["credits"].values()), int(student["id"]), student

def undecorate(decorated_student):
    # Discard the sum of credits, return original student dictionary
    return decorated_student[2]

def main():
    # print(students)
    sorted_students = sorted(map(decorate, students), reverse=True)
    print(sorted_students)
    print()
    sorted_students = list(map(undecorate, sorted_students))
    print(sorted_students)

if __name__ == '__main__':
    main()