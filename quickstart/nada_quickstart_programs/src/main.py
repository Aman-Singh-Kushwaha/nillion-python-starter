from nada_dsl import *

def nada_main():
    # Define the party for the class (teacher or attendance manager)
    class_teacher = Party(name="Class Teacher 🏫")

    # Define secret inputs for the attendance status of students
    student_1_attendance = SecretBoolean(Input(name="student_1_attendance", party=class_teacher))
    student_2_attendance = SecretBoolean(Input(name="student_2_attendance", party=class_teacher))
    student_3_attendance = SecretBoolean(Input(name="student_3_attendance", party=class_teacher))

    # Define secret inputs for the current total attendance counts
    student_1_total_attendance = SecretInteger(Input(name="student_1_total_attendance", party=class_teacher))
    student_2_total_attendance = SecretInteger(Input(name="student_2_total_attendance", party=class_teacher))
    student_3_total_attendance = SecretInteger(Input(name="student_3_total_attendance", party=class_teacher))

    # Update attendance counts based on today's attendance status
    updated_attendance_count_1 = student_1_attendance.if_else(student_1_total_attendance + 1, student_1_total_attendance)
    updated_attendance_count_2 = student_2_attendance.if_else(student_2_total_attendance + 1, student_2_total_attendance)
    updated_attendance_count_3 = student_3_attendance.if_else(student_3_total_attendance + 1, student_3_total_attendance)

    # Output the updated attendance counts for each student
    final_attendance_count_1 = Output(updated_attendance_count_1, "final_attendance_count_1", class_teacher)
    final_attendance_count_2 = Output(updated_attendance_count_2, "final_attendance_count_2", class_teacher)
    final_attendance_count_3 = Output(updated_attendance_count_3, "final_attendance_count_3", class_teacher)

    # Output the attendance status for the day
    attendance_status_1 = Output(student_1_attendance, "attendance_status_1", class_teacher)
    attendance_status_2 = Output(student_2_attendance, "attendance_status_2", class_teacher)
    attendance_status_3 = Output(student_3_attendance, "attendance_status_3", class_teacher)

    return [
        final_attendance_count_1,
        final_attendance_count_2,
        final_attendance_count_3,
        attendance_status_1,
        attendance_status_2,
        attendance_status_3
    ]