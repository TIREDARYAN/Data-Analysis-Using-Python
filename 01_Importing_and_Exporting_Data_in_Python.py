# Process of loading and reading data in python from various resources.

'''TWO IMPORTANT PROPERTIES'''
# Format -> Format is the way the data is encoded. We can usually tell different encoding schemes by looking at the ending of the file name.
    #Various formats: .CSV, .json, .xlsx, .hdf ...

# File Path of dataset -> The path usually tell where data stores. 
    # Computer:/Desktop/mydata.csv (On the computer)
    # https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data (Online Dataset)

# CSV - Comma Seprated Values.

'''
[Importing a CSV INTO Python]

import pandas as pd

--File Path
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

--Read CSV Method to import the data
df = pd.read_csv(url)


--However, read csv assume the data contain a header but our data on used car have no headers.
--So, we need to specify the read CSV to not assign the headers by setting header to none. 

df = pd.read_csv(url, header = None)
'''

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)



'''[ADDING HEADER TO THE DATAFRAME]'''
# Add column names manually since there's no header
headers = ["symboling","normalized-losses","make","fuel-type","aspiration",
           "num-of-doors","body-style","drive-wheels","engine-location",
           "wheel-base","length","width","height","curb-weight","engine-type",
           "num-of-cylinders","engine-size","fuel-system","bore","stroke",
           "compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers


"""
[PRINTING THE DATAFRAME IN PYTHON]

# df prints the entire dataframe (not recommended for large datasets)
--Since, printing the entire dataframe take too much time and resources.

--To save time
df.head(n) to show the first n rows of the data frame.

--Similarly
df.tail(n) to show the bottom n rows of the data frame.
"""

print(df.head(5))  # <-- add print() so it displays in terminal


"""
[Exporting a Pandas dataframe to CSV] --Preserve Progress anytime by saving modified dataset using

--At some point in time, after you've done operation on your data frame.
--You may want to export your pandas data frame to a new CSV file.

path = r"D:\Data_Science\saved_data\automobile.csv" --Specify the path which include the file name
df.to_csv(path)

"""

path = r"D:\Data_Science\saved_data\automobile.csv"
df.to_csv(path)

"""
[However Exporting to different format in python]

Data Fromat     Read                save
csv             pd.read_csv()       df.to_csv()
json            pd.read_json()      df.to_json()
Excel           pd.read_excel()     df.to_excel()
sql             pd.read_sql()       df.to_sql()

"""