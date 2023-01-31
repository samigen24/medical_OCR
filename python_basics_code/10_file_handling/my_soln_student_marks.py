'''
lineNumber = 0
student_info = {}
i = 1
with open("student_marks.csv", "r") as f:
    for line in f:
        student_details = line.split(',')
        student_info[i] = {'name': student_details[0]}
        student_info[i].update({'Gender': student_details[1]})
        student_info[i].update({'DOB': student_details[2]})
        student_info[i].update({'Maths': student_details[3]})
        student_info[i].update({'Physics': student_details[4]})
        student_info[i].update({'Chemistry': student_details[5]})
        student_info[i].update({'English': student_details[6]})
        student_info[i].update({'Biology': student_details[7]})
        student_info[i].update({'Economics': student_details[8]})
        student_info[i].update({'History': student_details[9]})
        student_info[i].update({'Civics': student_details[10]})
        print("\n")
        i += 1

    print(student_info)



collection = {}
i = 1
with open("student_marks.csv", "r") as f:
    for line in f:
        word = line.split(',')
        a = word[0]
        b = {'Gender': word[1]}
        b.update({'DOB': word[2]})
        b.update({'Maths': word[3]})
        b.update({'Physics': word[4]})
        b.update({'Chemistry': word[5]})
        b.update({'English': word[6]})
        b.update({'Biology': word[7]})
        b.update({'Economics': word[8]})
        b.update({'History': word[9]})
        b.update({'Civics': word[10]})
        b.update({'Total': int[word[3]]})
        collection[a] = b

    print(collection)



collection = {}
i = 1
with open("student_marks.csv", "r") as f:
    for line in f:
        word = line.split(',')
        n = len(word)
        a = word[0]
        b = {'Gender': word[1]}
        b.update({'DOB': word[2]})

        c = ({'Maths': word[3]})
        c.update({'Physics': word[4]})
        c.update({'Chemistry': word[5]})
        c.update({'English': word[6]})
        c.update({'Biology': word[7]})
        c.update({'Economics': word[8]})
        c.update({'History': word[9]})
        c.update({'Civics': word[10]})
        c.update({'Total': word[3]})

        collection[a] = b
        collection[a].update(c)

    print(collection)

'''


collection = {}
i = 0
with open("student_marks.csv", "r") as f:
    for line in f:
        i += 1
        if i > 1:
            word = line.split(',')
            a = word[0]
            b = word[1:3]

            c = word[3:11]
            d = len(c)-1
            c = c[0:d]

            collection[a] = b + c

    print(collection)


