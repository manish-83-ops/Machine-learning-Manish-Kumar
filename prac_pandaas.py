import pandas as pd 
data = [100,200,300,400,600]

series = pd.Series(data, index=["a","b","c","d","e"])
print(series[series>=200])

data1= {"Name": ["manish","ayush","ram","rahul"], "AGE":
    [18,20,30,90]}
df= pd.DataFrame(data1)

print(df.loc[1])
#new column addition 
df["job"] = ["w","e","y","y"]


#new row add krna
row1=pd.DataFrame([{"Name" :"sandy","AGE":28,"job":"t"}])#all attributes must be same like Nmae , AGE, job
df= pd.concat([df,row1])
print(df)