course_name_1 = input('Enter first course name')
course_name_2 = input('Enter second course name')
course_name_3 = input('Enter third course name')
course_1_grade = int(input('The %s course grade is\n' % course_name_1))
course_2_grade = int(input('The %s second course grade\n' % course_name_2))
course_3_grade = int(input('The %s third course grade is\n' % course_name_3))
total = course_1_grade + course_2_grade + course_3_grade
average = total / 3
print('The total is %s' % total)
print('The average is %s' % average)
output_report = '''
              Report Card
  Course name               Course Grade
%s\n
    Python                          %s
    Math                            %s
    English                         %s
%s\n
    Total                           %s
    Average                         %s
''' % (47 * '-', course_1_grade, course_2_grade, course_3_grade,
	   47 * '=', total, average)
print(output_report)
