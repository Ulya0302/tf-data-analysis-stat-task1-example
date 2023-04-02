import pandas as pd
import numpy as np


chat_id = 418462076 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 40
    a = x * 2 / t**2
    return a.mean() # Ваш ответ
