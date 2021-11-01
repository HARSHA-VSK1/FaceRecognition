import datetime
with open('Attendance.csv','r+') as f:
    myDataList = f.readlines()
    print(myDataList)
    print(myDataList[0])
    nameList = []
    name="BharathChandra".upper()

    for line in myDataList:
        entry = line.split(',')
        #print(entry)
        nameList.append(entry[0])
        if name not in nameList:
            print(1)
            now = datetime.datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
