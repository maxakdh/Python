def computergrade (score) :
    if grade < 0.0:
        return 'Bad Score'
    elif grade > 1.0 :
         return 'Bad Score'
    elif grade >=0.9 :
        return 'A'
    elif grade >= 0.8 :
        return 'B'
    elif grade >= 0.7 :
        return 'C'
    elif grade >= 0.6 :
        return 'D'
    elif grade > 0.6 :
        return 'F'
    else:
        return 'Enter a numerical value' 

score = input('Enter Score: ')
try:
    grade = float(score)

except:
    grade = -1

cg = computergrade(score)
print(cg)






       
    
