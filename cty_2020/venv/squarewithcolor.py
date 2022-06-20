courseName = input("Enter Course Name ")
testScore = input('Enter test score ')
quizScore = input('''Enter quiz score ''')
assignmentScore = input("Enter assignment score")
totalScore = int(testScore) + int(quizScore) + int(assignmentScore)
print("Total score is %s" % totalScore)
comment = '''Great job in 
%s 
Happy coding'''
print(comment % courseName)