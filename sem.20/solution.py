import pandas

# a) отваря файла "students.csv", инициализиран към променлива от тип DataFrame

with open('students.csv') as file:

    # returns DataFrame
    df = pandas.read_csv(file)

# б) изчиства всички повтарящи се редове и редовете, съдържащи 'none'

    # removes duplicates
    df.drop_duplicates(inplace=True)

    # drop column 'id'
    df.drop("id", axis="columns", inplace=True)

    # drop all 'none' values in column TestPrep
    df = df[df.TestPrep != "none"]

# в) присвоява на нова променлива само редовете от таблицата, които съдържат group A от колоната EthnicGroup

    # returns rows with value "group A" in column "EthnicGroup"
    new_df = df[df.EthnicGroup == 'group A']
    print(new_df.to_string())  # по-красиво извеждане на таблицата в конзолата

# г) извежда в конзолата средната стойност на всички стойности в колоната MathScore

    # returns the column average from new_df
    print(new_df["MathScore"].mean())

# д) записва се таблицата в нов файл с име "student_groupA.csv"

    # creating new csv file
    new_df.to_csv("student_groupA.csv", index=False)
