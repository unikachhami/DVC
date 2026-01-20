import pandas as pd
import os

data = {'Name':['AB','CD','EF'],
        'Age':[1,2,3],
        'Address':['l','M','N']
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,"Sample.csv")

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")