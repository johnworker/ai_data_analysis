import pandas as pd

def load_data(file_path):
    """讀取 CSV 檔案並回傳 DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print(f"成功讀取數據，共 {df.shape[0]} 筆資料")
        return df
    except Exception as e:
        print(f"讀取失敗: {e}")
        return None
