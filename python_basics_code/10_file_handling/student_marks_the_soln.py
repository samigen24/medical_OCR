
with open("student_marks.csv", "r") as f:
    #print(f.read())
    f.seek(0)  # go to the start again
    d = {}
    keys = f.readline()  # takes only the first line
    # print(keys)

    keys = keys.split(',')
    # print(keys)
    for key in keys:
        d[key] = []
    print(d)

    for line in f.readlines():  # the readlines here takes the remaining lines
        data = line.split(',')
        # print(data)
        j = 0
        for i in d:
            d[i].append(data[j])
            j += 1
    print(d)

    print(d.values())

    d['Total Marks'] = [0]*5
    for i in range(5):
        for key in d:
            try:
                d['Total Marks'][i] += int(d[key][i])
            except:
                pass
    print(d['Total Marks'])
    print(d)

    # import csv
    # fields = d[key]
    #
    # filename = "student_totals.csv"
    #
    # with open("student_totals.csv", "w") as file:
    #     d_writer = csv.DictWriter(file, fieldnames = fields)
    #     d_writer.writeheader()
    #     d_writer.writerows()









