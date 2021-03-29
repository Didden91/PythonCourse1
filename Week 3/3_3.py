score = input("Please enter your score (between 0.0 and 1.0): ")
try:
    score = float(score)
except:
    print("Input error")
    quit()

if score < 0:
    print ("Error, your score is below 0")
elif score >= 0 and score < 0.6:
    print ("F")
elif score >= 0.6 and score < 0.7:
    print ("D")
elif score >= 0.7 and score < 0.8:
    print ("C")
elif score >= 0.8 and score < 0.9:
    print ("B")
elif score >= 0.9 and score <= 1.0:
    print ("A")
else:
    print ("Error, your score is too high")
