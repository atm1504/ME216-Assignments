# Code to solve pipe network problem. Assignment 2
# The code has been written by Amartya Mondal. It has not been copied from anywhere. So all copyrights are reserved by atm1504.
# For more info visit:
# GitHub: https://github.com/atm1504/ME216-Assignments
# Website: https://atm1504.in

error = 0.000001
Qab=40
Qad = 20
Qbd = 15
Qbc = 25
Qcd = 15
Rab =4
Rad =5
Rbd =8
Rbc =5
Rcd = 6
e1 = e2 = 1
i = 1
# Print the header
print("Iteration Number", "Qab", "Qad", "Qbd", "Qbc", "Qcd")
# Loop to find the value
while (e1 > error or e2 > error):
    print(i, Qab, Qad, Qbd, Qbc, Qcd)
    # For loop 1
    num1 = Rab * abs(Qab) * Qab + Rbd * abs(Qbd) * Qbd - Rad * abs(Qad) * Qad
    den1 = 2 * (Rab * abs(Qab) + Rbd * abs(Qbd) + Rad * abs(Qad))
    dq1 = num1 / den1
    e1 = num1

    # For loop 2
    num2 = Rbc * abs(Qbc) * Qbc - Rcd * abs(Qcd) * Qcd - Rbd * abs(Qbd) * Qbd
    den2 = 2 * (Rbc * abs(Qbc) + Rcd * abs(Qcd) + Rbd * abs(Qbd))
    dq2 = num2 / den2
    e2 = num2

    # Update the elements
    Qab -= dq1
    Qad += dq1
    Qbd -= (dq1 - dq2)
    Qbc -= dq2
    Qcd += dq2
    i += 1