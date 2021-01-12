import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName])

def lastNameBusSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName, ['StLastName', 'StFirstName', 'Bus']])

def teacherSearch(df, TLName, TFName):
    print(df[(df['TLastName']==TLName) & (df['TFirstName']==TFName)])

def busSearch(df, busNum):
    print(df.loc[df['Bus'] == busNum])

def gradeSearch(df, grade):
    print(df.loc[df['Grade'] == grade])

def main():
    data_dir = "students.txt"
    df_students = pd.read_csv(data_dir, header=None, names=['StLastName', 'StFirstName', 
        'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
<<<<<<< HEAD
    lastNameBusSearch(df_students, "CORKER")
=======
    gradeSearch(df_students, 2)
>>>>>>> 579c90dd7692dadbdbd6e42098900ccc3d5d7134

if __name__ == "__main__":
    main()