import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

# ==========================================
# Mission 1: 造数据 (升级版：生成4年数据)
# ==========================================
# 修复点：把开始时间从 2024 改成 2022，保证数据量充足
# ------------------------------------------
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', end='2025-12-31', freq='D')

# 模拟业务逻辑
base_sales = 100
# 趋势：4年时间，销量稳步增长
trend = np.linspace(0, 100, len(dates))
# 季节性：乘以8代表4年里有4个完整的正弦波 (3.14 * 2 = 1个周期)
seasonality = 30 * np.sin(np.linspace(0, 3.14 * 2 * 4, len(dates)))
noise = np.random.normal(0, 10, len(dates))

sales_data = base_sales + trend + seasonality + noise
final_sales = np.maximum(sales_data, 0).astype(int)

df = pd.DataFrame({'Date': dates, 'Sales_Quantity': final_sales})
df.set_index('Date', inplace=True)

# ==========================================
# Mission 2: 数据清洗与分析
# ==========================================
# 宏观：月度汇总
monthly_sales = df['Sales_Quantity'].resample('ME').sum()
# 微观：7天移动平均
df['7_Day_MA'] = df['Sales_Quantity'].rolling(window=7).mean()

print("--- 数据准备完成，共有 {} 天的数据 ---".format(len(df)))

# ==========================================
# Mission 3: 预测未来 (Forecasting)
# ==========================================
print("\n--- 开始构建预测模型 (Holt-Winters) ---")

# 1. 划分训练集和测试集 (还是藏起最后30天)
train_data = df['Sales_Quantity'].iloc[:-30]
test_data = df['Sales_Quantity'].iloc[-30:]

# 2. 建立模型
# 这次我们的训练数据有 1400+ 天，远远超过 730 天，绝对不会报错了
model = ExponentialSmoothing(
    train_data,
    seasonal_periods=365,  # 告诉模型：一年一个轮回
    trend='add',
    seasonal='add',
    use_boxcox=False,
    initialization_method="estimated"
).fit()

# 3. 预测未来30天
forecast = model.forecast(30)

# 4. 评估准确度
mae = mean_absolute_error(test_data, forecast)
print(f"✅ 模型运行成功！")
print(f"平均绝对误差 (MAE): {mae:.2f} 件")

# 5. 可视化最终结果
plt.figure(figsize=(12, 6))
# 画最近半年的历史数据，不然图太挤了
plt.plot(train_data.index[-180:], train_data.iloc[-180:], label='History (Train)', color='gray', alpha=0.5)
plt.plot(test_data.index, test_data, label='Actual Sales (Test)', color='blue', linewidth=2)
plt.plot(test_data.index, forecast, label='Forecast (AI Prediction)', color='orange', linestyle='--', linewidth=3)
plt.title(f'Logistics Demand Forecast (MAE: {mae:.2f})')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.legend()
plt.grid(True)
plt.show()
