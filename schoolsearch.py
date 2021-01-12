import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName,
        ['StLastName', 'StFirstName', 'Grade', 'Classroom', 'TLastName', 'TFirstName']])

def lastNameBusSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName, 
        ['StLastName', 'StFirstName', 'Bus']])

def teacherSearch(df, TLName, TFName):
    print(df.loc[(df['TLastName']==TLName) & (df['TFirstName']==TFName), 
        ['StLastName', 'StFirstName']])

def busSearch(df, busNum):
    print(df.loc[df['Bus'] == busNum,
        ['StLastName', 'StFirstName', 'Grade', 'Classroom']])

def gradeSearch(df, grade):
    print(df.loc[df['Grade'] == grade,
        ['StLastName', 'StFirstName']])

def avgGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade]
    print("Grade \tAverage GPA")
    print(grade, " \t", new_df["GPA"].mean())

def lowestGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade,
        ['StLastName', 'StFirstName', 'GPA', 'TLastName', 'TFirstName', 'Bus']]
    minGPA = new_df["GPA"].min()
    print(new_df.loc[new_df['GPA'] == minGPA])

def highestGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade,
        ['StLastName', 'StFirstName', 'GPA', 'TLastName', 'TFirstName', 'Bus']]
    maxGPA = new_df["GPA"].max()
    print(new_df.loc[new_df['GPA'] == maxGPA])

def numStudents(df):
    #print((df['Grade'].value_counts()).reindex(df.Grade.unique(), fill_value = 0))
    grades = df.Grade.unique()
    check = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        if i not in grades:
            check[i] = 1
     

def main():
    data_dir = "students.txt"
    df_students = pd.read_csv(data_dir, header=None, names=['StLastName', 'StFirstName', 
        'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
    
    quit = False
    while not quit:
        command = str(input("Type your command: "))
        split = command.split()
        if split[0]=="S:" or split[0]=="Student:":
            lastName = split[1]
            if len(split) != 3:
                lastNameSearch(df_students, lastName)
            elif len(split) == 3 and (split[2] == "B" or split[2] == "Bus"):
                lastNameBusSearch(df_students, lastName)
        elif split[0]=="Teacher:" or split[0]=="T:":
            lastName = split[1]
            teacherSearch(df_students, lastName)
        elif split[0]=="B:" or split[0]=="Bus:":
            number = int(split[1])
            busSearch(df_students, number)
        elif split[0]=="Grade:" or split[0]=="G:":
            number = int(split[1])
            if len(split) != 3:
                gradeSearch(df_students, number)
            elif split[2]=="High" or split[2]=="H":
                highestGPA(df_students, number)
            elif split[2]=="Low" or split[2]=="L":
                lowestGPA(df_students, number)
        elif split[0]=="A:" or split[0]=="Average:":
            number = int(split[1])
            avgGPA(df_students, number)
        elif split[0]=="I" or split[0]=="Info":
            numStudents(df_students)
        elif split[0]=="Q" or split[0]=="Quit":
            quit = True

    #lastNameSearch(df_students, "CORKER")
    #lastNameSearch(df_students, "COMO")
    #lastNameBusSearch(df_students, "CORKER")
    #lastNameBusSearch(df_students, "COMO")
    #teacherSearch(df_students, "CHIONCHIO", "PERLA")
    #teacherSearch(df_students, "COOL", "REUBEN")
    #gradeSearch(df_students, 1)
    #gradeSearch(df_students, 3)
    #busSearch(df_students, 52)
    #busSearch(df_students, 56)
    #avgGPA(df_students, 1)
    #avgGPA(df_students, 3)
    #lowestGPA(df_students, 3)
    #lowestGPA(df_students, 1)
    #highestGPA(df_students, 3)
    #highestGPA(df_students, 1)
    numStudents(df_students)

if __name__ == "__main__":
    main()