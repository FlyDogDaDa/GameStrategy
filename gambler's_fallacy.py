import numpy as np


def create_bool_array(n):
    """
    建立一個布林值的 1D 陣列，長度為 n，True 的機率為 1/2。

    參數：
      n: 陣列的長度，必須是正整數。

    回傳：
      一個布林值的 NumPy 陣列，長度為 n，每個元素隨機為 True 或 False。
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n 必須是正整數")
    return np.random.choice([True, False], size=n)


n = int(1e7)
c = 10
w = n - c
array = create_bool_array(n)
arr_win = np.lib.stride_tricks.sliding_window_view(array, c)
continuously = np.logical_not(arr_win.any(axis=1))[:-1]
cont_count = np.sum(continuously)
print("採樣數量:", n)
print("連續F數量:", cont_count)
print("連續F比例:", round(cont_count / w * 100, 2), "%")
hit = array[c:][continuously]
print("連續F之後出現T:", round(np.sum(hit) / len(hit) * 100, 2), "%")
