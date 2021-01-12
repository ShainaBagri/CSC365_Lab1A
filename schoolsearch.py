import pandas as pd

def lastNameSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName])

def lastNameBusSearch(df, lastName):
    print(df.loc[df['StLastName'] == lastName, ['StLastName', 'StFirstName', 'Bus']])

def teacherSearch(df, TLName):
    print(df[df['TLastName']==TLName])

def busSearch(df, busNum):
    print(df.loc[df['Bus'] == busNum])

def gradeSearch(df, grade):
    print(df.loc[df['Grade'] == grade])

def avgGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade]
    print(new_df["GPA"].mean())

def lowestGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade]
    print(new_df["GPA"].min())

def highestGPA(df, grade):
    new_df = df.loc[df['Grade'] == grade]
    print("Min GPA: " + new_df["GPA"].max())

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
        elif split[0]=="Grade:" or split[0]=="G:":
            number = split[1]
            gradeSearch(df_students, number)
        elif split[0]=="B:" or split[0]=="Bus:":
            number = split[1]
            busSearch(df_students, number)
        elif split[0]=="Grade:" or split[0]=="G:":
            number = split[1]
            if split[2]=="High" or split[2]=="H":
                highestGPA(df_students, number)
            elif split[2]=="Low" or split[2]=="L":
                lowestGPA(df_students, number)
        elif split[0]=="Q" or split[0]=="Quit":
            quit = True



                
                




if __name__ == "__main__":
    main()