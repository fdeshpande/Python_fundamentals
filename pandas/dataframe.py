import pandas as pd
capital=[]
small =[]
askii_s =[]
askii_c =[]
for i in range(65,122+1):
    if i not in [91,92,93,94,95,96]:
        if chr(i).isupper():
            askii_c.append(i)
            capital.append(chr(i))
        else:
            askii_s.append(i)
            small.append(chr(i))

d={'ASCII for uppercase':askii_c,'Uppercase character':capital,'ASCII for lowercase':askii_s,'Lowercase character':small }

df = pd.DataFrame(d)
df.to_csv('alphabet.csv',index=False)

file_path =r"C:\Users\deshp\OneDrive\Desktop\PracticePython projects\PracticePython projects\pandas\alphabet.csv"
df = pd.read_csv(file_path)
# print(df)
# to diplay the few lines of code in df
df = pd.read_csv(file_path)
print(df.head(3))

# to get the shape/size of dataframe
r,c = df.shape
print(r,c)

# to get basic statistics of dataframe

statistics=df.describe()
print(statistics)

# to get missing values in df

miss_values = df.isnull().sum()
print(miss_values)

# to select a single column for df
print(df['ASCII for lowercase'])


# to select a row based on conditions

print(df[df['ASCII for lowercase']>7])

# to select rows and columns symultaneously

print(df.loc[[2,5],['Lowercase character','ASCII for lowercase']])

# add new column to df

df['id'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
print(df)

# rename column name

df.rename(columns={'id':'id_'},inplace=True)
print(df)

# to drop a column
# df.drop(columns='id_',inplace=True)
# print(df)

# Sorting the DataFrame by a Specific Column:

sorted_df=df.sort_values(by='id_')
print(sorted_df)

# Finding Unique Values in a Column:

unique_values = df['id_'].unique()
print(unique_values)


# merging two dfs
# merged_df = pd.merge(df1, df2, on='CommonColumn', how='inner')
#
# # Display the merged DataFrame
# print("Merged DataFrame:")
# print(merged_df)


# concatinate virtically dfs

# vc = pd.concat([df1,df2],axis=0)
# concatinate horizontally dfs

# vc = pd.concat([df1,df2],axis=1)

# drop rows with NA values

df.dropna()

# filled with any value
df.fillna(0)

# detect duplicate values based on one coluns
dup=df[df['id_']].drop_duplicates()

# detect duplicates
df.drop_duplicates()