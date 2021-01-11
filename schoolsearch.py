import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName' == lastName]])

def lastNameBusSearch(df, lastName):
    df_new = df.loc[df['StLastName' == lastName]]
    for index, row in df_new.iterrows():
        print(index, row)

def teacherSearch(df, TLName, TFName):
    #print(df.query('TLastName=="TLName" & TFirstName=="TFName" ', inplace=True))
    print(df.loc[df['TLastName' == TLName], df['TFirstName' == TFName]])


def main():
    data_dir = "students.txt"
    df_students = pd.read_csv(data_dir, header=None, names=['StLastName', 'StFirstname', 
        'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
    lastNameBusSearch(df_students, "Corker")

if __name__ == "__main__":
    main()