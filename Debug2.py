def score_to_letter_grade(grade):   #this function return a grade according to score 
    if grade >= 90: #if score in greater or equals to 90 return A
        return "A"
    elif grade >= 87:   #if score in greater or equals to 87 return B+
        return "B+"
    elif grade >= 80:   #if score in greater or equals to 80 return B
        return "B"
    elif grade >= 77:
        return "C+"
    elif grade >= 70:
        return "C"
    elif grade >= 67:
        return "D+"
    elif grade >= 60:
        return "D"
    else:
        return "F"  #otherwise return F 

print("Grade of 90 should be A: " + score_to_letter_grade(90))  #call score_to_letter_grade function and print output 
print("Grade of 87 should be B+: " + score_to_letter_grade(87))
print("Grade of 81 should be B: " + score_to_letter_grade(81))
print("Grade of 77 should be C+: " + score_to_letter_grade(77))
print("Grade of 70 should be C: " + score_to_letter_grade(70))
print("Grade of 67 should be D+: " + score_to_letter_grade(67))
print("Grade of 60 should be D: " + score_to_letter_grade(60))
print("Grade of 59 should be F: " + score_to_letter_grade(59))
