pupil=int(input("enter the number of pupil that has attended:"))
sweets=int(input("enter the number of sweets we have:"))
distributed_sweets=sweets//pupil
left_sweets=sweets%pupil
print(f"each pupil must recieve {int(distributed_sweets)} sweets and you will have {left_sweets} sweets left.")