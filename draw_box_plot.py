import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


csv_name = ['0722test2_1.csv', '0722test2_2.csv', '0722test2_5.csv', '0722test2_3.csv']
x_list = []

for name in csv_name:
    df = pd.read_csv(name)
    x_list.append(df['error'].fillna(0).tolist())

print(x_list)
labels = ['A_Fast', 'A_Slow', 'B_Fast', 'B_Slow']
colors = ['lightblue', 'lightblue', 'lightgreen', 'lightgreen']
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

# ax.set_title("Box Plot")
ax.set_ylabel("Absolute Angle Difference (Degrees)")
boxplot = ax.boxplot(x_list, labels=labels, patch_artist=True)

for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
# ax.grid(True, axis='y')

plt.show()
