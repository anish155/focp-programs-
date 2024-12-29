students=int(input("how many students?"))
group=int(input("Required group size?"))
group_student=students//group
left_students=students%group
print(f"there will be {group_student} groups with {left_students} students left over.")