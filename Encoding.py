import os
import pandas as pd
import numpy as np

cwd = os.getcwd()
Input_dir = 'Input'
Output_dir='Output'
txt_path=os.path.join(cwd,Output_dir,'Test.txt')
Input_list = ['Machine','Process','Production_amount']
csv_path_list = [os.path.join(cwd,data_dir,f'{Input}.csv') for Input in Input_list]

df_Machine = pd.read_csv(csv_path_list[0])
df_Process = pd.read_csv(csv_path_list[1])
df_Production_amount = pd.read_csv(csv_path_list[2])

file = open(txt_path,'w')

job_process = [df_Production_amount['Amount'].sum(), len(df_Machine) ]
Product_type = list(df_Process['Type'].unique())
file.write('%i ' %job_process[0])
file.write('%i\n' %job_process[1])

for i in range(len(Product_type)):
    L=[]
    j_amt = df_Production_amount[df_Production_amount['Type']==Product_type[i]]['Amount'][i]
    p_temp = df_Process[df_Process['Type']==Product_type[i]].reset_index(drop=True)
    p_amt = len(p_temp)
    L.append(p_amt)
    for j in range(p_amt):
        L.append(p_temp.iloc[j,1])
        L.append(p_temp.iloc[j,2])
    for _ in range(j_amt):
        for j in range(int(len(L)-1)):
            file.write('%i ' %L[j])
        file.write('%i\n' %L[-1])

for i in range(len(df_Machine)):
    if i!=len(df_Machine)-1:
        file.write('%i\n' %df_Machine.iloc[i,1])
    else:
        file.write('%i' %df_Machine.iloc[i,1])
    
    
file.close()        