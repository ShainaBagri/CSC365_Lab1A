import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName' == lastName]])

def lastNameBusSearch(df, lastName):
    df_new = df.loc[df['StLastName' == lastName]]

def teacherSearch(df, TLName, TFName):
    print(df[(df['TLastName']==TLName) & (df['TFirstName']==TFName)])

def busSearch(df, busNum):
    print(df.loc[df['Bus'] == busNum])

def main():
    data_dir = "students.txt"
    df_students = pd.read_csv(data_dir, header=None, names=['StLastName', 'StFirstname', 
        'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
    busSearch(df_students, 52)

if __name__ == "__main__":
    main()