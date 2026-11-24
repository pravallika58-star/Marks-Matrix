# Marks-Matrix
# Student Marks Matrix Analysis

## Python Activity-Based Learning

### Student Details

- **Name:** DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

Student Marks Matrix Analysis is a Python-based program that analyses a matrix of student marks across multiple subjects.

The program calculates row-wise and column-wise statistics, identifies top-performing students and detects subjects with low average performance.

It displays student-wise total marks, average marks, highest marks, lowest marks and subject-wise average marks.

## 2. Objectives

- To create a matrix of student marks.
- To calculate student-wise total and average marks.
- To identify the highest and lowest marks of each student.
- To calculate subject-wise average marks.
- To identify the top-performing student.
- To detect subjects with low average performance.
- To understand matrix operations using nested lists.

## 3. Assumptions

1. The number of students must be greater than zero.
2. The number of subjects must be greater than zero.
3. Marks must be between 0 and 100.
4. Each student has marks in all selected subjects.
5. A subject is considered to have low average performance if its average is below 75.
6. The top performer is identified using the highest overall average marks.
7. If multiple students have the same highest average, all are displayed.

## 4. Algorithm

1. Start the program.
2. Enter the number of students and subjects.
3. Validate the entered numbers.
4. Enter the subject names.
5. Enter each student's name.
6. Read marks for every subject.
7. Validate marks between 0 and 100.
8. Store marks in a nested list.
9. Display the complete marks matrix.
10. Calculate row-wise statistics:
    - Total marks
    - Average marks
    - Highest marks
    - Lowest marks
11. Identify the student with the highest average.
12. Calculate column-wise statistics.
13. Identify subjects with an average below 75.
14. Display the complete analysis report.
15. Stop the program.

## 5. Pseudocode

```text
START

INPUT number_of_students
INPUT number_of_subjects

IF either number <= 0
    DISPLAY Invalid input

ELSE

    INPUT subject names

    FOR each student

        INPUT student name

        FOR each subject
            INPUT marks

            WHILE marks < 0 OR marks > 100
                INPUT valid marks
            END WHILE

            STORE marks
        END FOR

    END FOR

    DISPLAY marks matrix

    FOR each student

        CALCULATE total marks
        CALCULATE average marks
        FIND highest marks
        FIND lowest marks

    END FOR

    FIND highest student average
    DISPLAY top performer

    FOR each subject

        CALCULATE subject total
        CALCULATE subject average

        IF average < 75
            DISPLAY Low Average Performance
        ELSE
            DISPLAY Good Average Performance
        END IF

    END FOR

END IF

STOP
```

## 6. Python Source Code

**File name:** `student_marks_matrix.py`

The complete Python implementation is available in this folder.

## 7. Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| 1 | Valid student marks | Matrix generated |
| 2 | All marks are 100 | Average is 100 |
| 3 | All marks are 0 | Average is 0 |
| 4 | Marks below 0 | Invalid marks rejected |
| 5 | Marks above 100 | Invalid marks rejected |
| 6 | Number of students is 0 | Invalid input |
| 7 | Subject average below 75 | Low performance detected |
| 8 | Two students have equal highest average | Both identified as top performers |

## 8. Expected Output

```text
STUDENT MARKS MATRIX ANALYSIS

STUDENT-WISE ANALYSIS

Student: Pravallika
Total Marks: 311
Average Marks: 77.75
Highest Marks: 88
Lowest Marks: 60

Student: Anu
Total Marks: 280
Average Marks: 70.0
Highest Marks: 80
Lowest Marks: 55

Student: Ravi
Total Marks: 346
Average Marks: 86.5
Highest Marks: 96
Lowest Marks: 65

TOP PERFORMER
Ravi - Average: 86.5

SUBJECT-WISE ANALYSIS

Python: 83.33
Mathematics: 60.0
English: 82.67
Physics: 86.33

Mathematics:
Low Average Performance

ANALYSIS COMPLETED
```

## 9. Conclusion

The Student Marks Matrix Analysis program successfully analyses student marks using Python nested lists and loops. It calculates student-wise and subject-wise statistics, identifies top performers and detects subjects with low average marks.

This project helps us understand Python variables, lists, nested lists, loops, conditional statements, arithmetic operators and built-in functions such as max() and min().

It also demonstrates how matrix-based data analysis can be used to evaluate academic performance.

---

**Project:** Python Activity-Based Learning  
**Topic:** Student Marks Matrix Analysis
