# --- Step 2 Mini Project: Student Profile & Marksheet Summary

# 1. Defining String     Variables
student_name = "Jay Pawar"
course_name = "BCA  Science"
college_name =   "ASM CSIT College"

# 2. Defining Integer Variables
roll_number = 101
total_subjects = 3

# 3. Defining Float Variables   (Marks out of 100)
c_programming_marks = 85.5  
cpp_programming_marks = 88.0
python_programming_marks = 92.5

# 4.     Calculation using Variables
total_marks = c_programming_marks + cpp_programming_marks + python_programming_marks
average_marks = total_marks / total_subjects

    # 5. Defining Boolean Variable based on condition
is_passed = average_marks >= 40.0

# 6. Displaying the Profile and Summary Output
print("     ==================================================")
print("             STUDENT PROFILE SUMMARY              ")
print("     ==================================================")
print(" Student Name :", student_name)
print(" Course       :", course_name)
print(" College      :", college_name)
print(" Roll Number  :", roll_number)
print("--------------------------------------------------")
print(" C Marks      :",    c_programming_marks)
print(" C++ Marks    :", cpp_programming_marks)
print(" Python Marks :", python_programming_marks)
print("--------------------------------------------------")
print(" Total Marks  :",    total_marks, "/ 300.0")
print(" Average      :", round(average_marks, 2))
print(" Passed Status:", is_passed)
print("==================================================")

# 7. Data Types Verification
print("\n--- Data Types Used in this Project ---")
print("student_name type :", type(student_name))
print("roll_number type  :", type(roll_number))
print("total_marks type  :", type(total_marks))
print("is_passed type    :", type(is_passed))
print("==================================================")