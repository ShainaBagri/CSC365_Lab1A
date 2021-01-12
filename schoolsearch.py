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