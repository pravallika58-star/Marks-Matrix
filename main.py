
# Student Marks Matrix Analysis

print("==========================================")
print("       STUDENT MARKS MATRIX ANALYSIS")
print("==========================================")

# Input number of students and subjects
students_count = int(input("Enter number of students: "))
subjects_count = int(input("Enter number of subjects: "))

if students_count <= 0 or subjects_count <= 0:
    print("Invalid input! Enter positive numbers.")

else:

    student_names = []
    subject_names = []
    marks = []

    # Input subject names
    print("\nEnter Subject Names:")

    for j in range(subjects_count):
        subject = input("Subject " + str(j + 1) + ": ")
        subject_names.append(subject)

    # Input student names and marks
    for i in range(students_count):

        print("\nEnter details of Student", i + 1)

        name = input("Student Name: ")
        student_names.append(name)

        student_marks = []

        for j in range(subjects_count):

            mark = int(input(
                "Enter marks in " + subject_names[j] + ": "
            ))

            while mark < 0 or mark > 100:
                print("Enter marks between 0 and 100.")
                mark = int(input(
                    "Enter marks in " + subject_names[j] + ": "
                ))

            student_marks.append(mark)

        marks.append(student_marks)

    # Display marks matrix
    print("\n==========================================")
    print("             MARKS MATRIX")
    print("==========================================")

    print("Student", end="\t")

    for subject in subject_names:
        print(subject, end="\t")

    print()

    for i in range(students_count):

        print(student_names[i], end="\t")

        for j in range(subjects_count):
            print(marks[i][j], end="\t")

        print()

    # Row-wise analysis
    print("\n==========================================")
    print("       STUDENT-WISE ANALYSIS")
    print("==========================================")

    averages = []

    for i in range(students_count):

        total = 0

        for j in range(subjects_count):
            total += marks[i][j]

        average = total / subjects_count
        averages.append(average)

        print("\nStudent:", student_names[i])
        print("Total Marks:", total)
        print("Average Marks:", round(average, 2))
        print("Highest Marks:", max(marks[i]))
        print("Lowest Marks:", min(marks[i]))

    # Identify top performer
    highest_average = max(averages)

    print("\n==========================================")
    print("           TOP PERFORMER")
    print("==========================================")

    for i in range(students_count):

        if averages[i] == highest_average:
            print(student_names[i],
                  "- Average:", round(averages[i], 2))

    # Column-wise analysis
    print("\n==========================================")
    print("       SUBJECT-WISE ANALYSIS")
    print("==========================================")

    low_found = False

    for j in range(subjects_count):

        total = 0

        for i in range(students_count):
            total += marks[i][j]

        average = total / students_count

        print("\nSubject:", subject_names[j])
        print("Total Marks:", total)
        print("Average Marks:", round(average, 2))

        if average < 75:
            print("Status: Low Average Performance")
            low_found = True
        else:
            print("Status: Good Average Performance")

    if not low_found:
        print("\nNo subjects have an average below 75.")

    print("\n==========================================")
    print("         ANALYSIS COMPLETED")
    print("==========================================")
