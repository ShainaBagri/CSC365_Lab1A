import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName' == lastName]])

def lastNameBusSearch(df, lastName):
    df_new = df.loc[df['StLastName' == lastName]]

def teacherSearch(df, TFName, TLName):
    print(df.loc[df[('TLastName' == TLName) and ('TFirstName' == TFName)]])

def main():
    data_dir = "students.txt"
    df_students = pd.read_csv(data_dir, header=None, names=['StLastName', 'StFirstname', 
        'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
    teacherSearch(df_students, "Rocio", "Fafard")

if __name__ == "__main__":
    main()