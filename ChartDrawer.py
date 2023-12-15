import matplotlib.pyplot as plt
import seaborn as sns

#seaborn scatter plot(nokta grafigi)

def plot_bar_chart(data, x_column, y_column, title, x_label, y_label):
    plt.figure(figsize=(10, 10))
    plt.bar(data[x_column], data[y_column], color='blue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_and_analyze_correlation(data,x_column,y_column,title,x_label,y_label):
    sns.scatterplot(x=x_column,y=y_column,data=data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

    #korelasyon katsayisi hesapla
    correlation=data[x_column].corr(data[y_column])
    print(f"Korelasyon Katsayısı ({x_column} ve {y_column}): {correlation}")