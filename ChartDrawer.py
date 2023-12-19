import os.path
import matplotlib.pyplot as plt
import seaborn as sns

"""
This script contains functions for data analysis and visualization.

1. `plot_bar_chart`: Function to create a bar chart. It draws a bar chart between specified columns in the given DataFrame.
2. `plot_and_analyze_correlation`: Function to analyze correlation between two columns by plotting a scatter plot. Additionally, it calculates the Pearson correlation coefficient.
3. `plot_pie_chart`: Function to create a pie chart. It draws a pie chart using the specified column in the given DataFrame.
"""

output_folder='Graphic_Analysis_Results'

##If the folder does not exist, it is created
if not os.path.exists((output_folder)):
    os.makedirs(output_folder)

def plot_bar_chart(data, x_column, y_column, title, x_label, y_label,file_name):
    plt.figure(figsize=(5, 5))
    plt.bar(data[x_column], data[y_column], color='blue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    file_path=os.path.join(output_folder,f"{file_name}.png")
    plt.savefig(file_path)
    #plt.show()


def plot_heatmap(data, title, file_name):
    # Korelasyon matrisini hesapla
    correlation_matrix = data[['Confirmed','Deaths','Recovered']].corr()

    # Heatmap çizimi
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt = '.2f')
    plt.title(title)

    # Heatmap'i dosyaya kaydet
    file_path = os.path.join(output_folder, f"{file_name}_heatmap.png")
    plt.savefig(file_path)
    plt.show()

def plot_pie_chart(data,title,file_name):
    plt.figure(figsize=(8,8))
    plt.pie(data,labels=data.index,autopct='%1.1f%%',startangle=140,shadow=True)
    plt.title(title)
    file_path=os.path.join(output_folder,f"{file_name}.png")
    plt.savefig(file_path)
   #plt.show()
