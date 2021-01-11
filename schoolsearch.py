import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName])

def lastNameBusSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName, ['StLastName', 'StFirstName', 'Bus']])

def teacherSearch(df, TLName, TFName):
    print(df[(df['TLastName']==TLName) & (df['TFirstName']==TFName)])


def main():
    data_dir = "students.txt"
    df_students = pd.read_csv(data_dir, header=None, names=['StLastName', 'StFirstName', 
        'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
    lastNameBusSearch(df_students, "CORKER")

if __name__ == "__main__":
    main()