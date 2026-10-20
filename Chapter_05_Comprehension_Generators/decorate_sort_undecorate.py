# Create a list of dictionaries to store students credits
students = [
        dict(id=0, credits=dict(math=9, physics=6, history=7)),
        dict(id=1, credits=dict(mth=6, physics=7, latin=10)),
        dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
        dict(id=3, credits=dict(math=5, physics=5, geography=7)),
        ]

def decorate(student):
    # create a tuple for the sum of credits of each student
    # Afterward, calculate the sum of the tuple elements
    # Return a 2-tuple with total credit and original student dictionary
    return sum(student["credits"].values()), student

def undecorate(decorated_student):
    # Discard the sum of credits, return original student dictionary
    # Would be the same as sorted_students[0][1]
    return decorated_student[1]

def main():
    # print(students)
    sorted_students = sorted(map(decorate, students), reverse=True)
    print(sorted_students)
    print()
    sorted_students = list(map(undecorate, sorted_students))
    print(sorted_students)

if __name__ == '__main__':
    main()