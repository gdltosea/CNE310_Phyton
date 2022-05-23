@@ -1,27 +1,21 @@
def score_to_letter_grade(grade):
    if grade > 90:
        return "A"
    elif grade >= 87:
        return "B+"
    elif grade == 80:
        return "B"
    elif grade >= 77:
        return "C+"
    elif grade <= 70:
        return "C"
    elif grade >= 67:
        return "D+"
    elif grade >= 60:
        return "D"
#function given in the question
def lone_sum(a, b, c):
    #sum contain the sum of 3 values in a,b and c
    sum = a + b + c
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return "F"
        return sum


print("Grade of 90 should be A: " + score_to_letter_grade(90))
print("Grade of 87 should be B+: " + score_to_letter_grade(87))
print("Grade of 81 should be B: " + score_to_letter_grade(81))
print("Grade of 77 should be C+: " + score_to_letter_grade(77))
print("Grade of 70 should be C: " + score_to_letter_grade(70))
print("Grade of 67 should be D+: " + score_to_letter_grade(67))
print("Grade of 60 should be D: " + score_to_letter_grade(60))
print("Grade of 59 should be F: " + score_to_letter_grade(59))
#input the values of a, b and c from the user
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
#function call
print(lone_sum(a,b,c) )
