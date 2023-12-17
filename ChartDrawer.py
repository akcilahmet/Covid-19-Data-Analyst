import os.path

import matplotlib.pyplot as plt
import seaborn as sns


output_folder='Graphic_Analysis_Results'

#eger klasör yok ise olusturma islemi yapilir
if not os.path.exists((output_folder)):
    os.makedirs(output_folder)

#seaborn scatter plot(nokta grafigi)
def plot_bar_chart(data, x_column, y_column, title, x_label, y_label,file_name):
    plt.figure(figsize=(10, 10))
    plt.bar(data[x_column], data[y_column], color='blue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    file_path=os.path.join(output_folder,f"{file_name}.png")
    plt.savefig(file_path)
    #plt.show()

def plot_and_analyze_correlation(data,x_column,y_column,title,x_label,y_label,file_name):
    sns.scatterplot(x=x_column,y=y_column,data=data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # Grafikleri farklı dosya adlarıyla kaydedin
    file_path=os.path.join(output_folder,f"{file_name}.png")
    plt.savefig(file_path)
   # plt.show()

    #korelasyon katsayisi hesapla
    correlation=data[x_column].corr(data[y_column])
    print(f"Korelasyon Katsayısı ({x_column} ve {y_column}): {correlation}")


def plot_pie_chart(data,title,file_name):
    plt.figure(figsize=(10,10))
    plt.pie(data,labels=data.index,autopct='%1.1f%%',startangle=140,shadow=True)
    plt.title(title)
    file_path=os.path.join(output_folder,f"{file_name}.png")
    plt.savefig(file_path)
   #plt.show()
