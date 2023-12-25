import pandas as pd

data = pd.read_excel('failure_probability.xlsx')
selected_data = data[data.iloc[:, 0] == 1000]

columns = selected_data.columns.tolist()[1:]
values = selected_data.values.tolist()[0][1:]

l = []

for i in range(len(columns)):
    l.append((columns[i], values[i]))

l = {columns[x]: values[x] for x in range(len(columns))}

print(l)


