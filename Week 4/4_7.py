
def computegrade (score):
    if score < 0:
        print ("Error, your score is below 0")
    elif score >= 0 and score < 0.6:
        return 'F'
    elif score >= 0.6 and score < 0.7:
        return 'D'
    elif score >= 0.7 and score < 0.8:
        return 'C'
    elif score >= 0.8 and score < 0.9:
        return 'B'
    elif score >= 0.9 and score <= 1.0:
        return 'A'
    else:
        return 'Error, your score is too high'


score = input("Please enter your score (between 0.0 and 1.0): ")

try:
    score = float(score)
except:
    print("Input error")
    quit()

grade = computegrade(score)
print(grade)
