from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_visualization import plot_histogram

def main():
    file_path = "data/raw/sample_data.csv"
    df = load_data(file_path)
    
    if df is not None:
        df = clean_data(df)
        plot_histogram(df, "數據欄位名稱")  # 替換成適當欄位名稱

if __name__ == "__main__":
    main()
