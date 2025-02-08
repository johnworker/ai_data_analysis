import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    """繪製直方圖"""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f'{column} 數據分佈')
    plt.show()
