import pandas as pd

# Прочитај ги податоците од combined_data.csv
df = pd.read_csv('combined_data.csv')

# Обработи ја колоната 'last_transaction_price' за да се направи број (замени запирки со точки за децимали и отстрани точките за илјадници)
df['last_transaction_price'] = df['last_transaction_price'].replace({',': '.'}, regex=True)  # Замени запирки со точки
df['last_transaction_price'] = df['last_transaction_price'].replace({'\\.' : ''}, regex=True)  # Отстрани точките за илјадници
df['last_transaction_price'] = df['last_transaction_price'].astype(float)  # Конвертирај во float

# Проверка на првите неколку редови на податоците
print(df.head())

# Пресметај SMA (Simple Moving Average) за 14 дена
df['SMA_14'] = df['last_transaction_price'].rolling(window=14).mean()

# Пресметај EMA (Exponential Moving Average) за 14 дена
df['EMA_14'] = df['last_transaction_price'].ewm(span=14, adjust=False).mean()

# Пресметај RSI (Relative Strength Index) за 14 дена
delta = df['last_transaction_price'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()

rs = gain / loss
df['RSI_14'] = 100 - (100 / (1 + rs))

# Пресметај MACD (Moving Average Convergence Divergence)
ema_12 = df['last_transaction_price'].ewm(span=12, adjust=False).mean()
ema_26 = df['last_transaction_price'].ewm(span=26, adjust=False).mean()
df['MACD'] = ema_12 - ema_26
df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

# Пресметај Bollinger Bands (BB)
df['BB_upper'] = df['SMA_14'] + (df['last_transaction_price'].rolling(window=14).std() * 2)
df['BB_lower'] = df['SMA_14'] - (df['last_transaction_price'].rolling(window=14).std() * 2)

# Пример на логика за генерирање на сигнали за купување, продажба или задржување акции
def generate_signals(row):
    if row['last_transaction_price'] > row['BB_upper']:
        return 'Sell'
    elif row['last_transaction_price'] < row['BB_lower']:
        return 'Buy'
    else:
        return 'Hold'

# Применување на функцијата за секој ред
df['Signal'] = df.apply(generate_signals, axis=1)

# Принтирање на резултатите
print(df[['date', 'last_transaction_price', 'SMA_14', 'EMA_14', 'RSI_14', 'MACD', 'Signal_Line', 'BB_upper', 'BB_lower', 'Signal']])

# Запиши ги резултатите во нов CSV фајл
df.to_csv('technical_analysis_results.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
csv_file_path = "combined_data.csv"
df = pd.read_csv(csv_file_path)

# Clean and preprocess the data
df['last_transaction_price'] = df['last_transaction_price'].str.replace(',', '').astype(float)

# Add technical indicators (without talib)

# Simple Moving Average (SMA)
def calculate_sma(data, period):
    return data.rolling(window=period).mean()

df['SMA_14'] = calculate_sma(df['last_transaction_price'], 14)

# Relative Strength Index (RSI)
def calculate_rsi(data, period):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['RSI_14'] = calculate_rsi(df['last_transaction_price'], 14)

# Bollinger Bands
def calculate_bollinger_bands(data, period):
    sma = calculate_sma(data, period)
    rolling_std = data.rolling(window=period).std()

    upper_band = sma + (2 * rolling_std)
    lower_band = sma - (2 * rolling_std)
    return upper_band, sma, lower_band

df['BB_upper'], df['BB_middle'], df['BB_lower'] = calculate_bollinger_bands(df['last_transaction_price'], 14)

# Generate trading signals based on SMA
conditions = [
    (df['last_transaction_price'] > df['SMA_14']),
    (df['last_transaction_price'] < df['SMA_14'])
]
choices = ['Buy', 'Sell']
df['Signal'] = pd.Series(['Hold'] * len(df))  # Default signal

df.loc[conditions[0], 'Signal'] = choices[0]
df.loc[conditions[1], 'Signal'] = choices[1]

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(df['last_transaction_price'], label='Last Transaction Price', color='blue')
plt.plot(df['SMA_14'], label='SMA 14', color='orange')
plt.fill_between(range(len(df)), df['BB_upper'], df['BB_lower'], color='gray', alpha=0.2, label='Bollinger Bands')
plt.legend(loc='best')
plt.title('Stock Analysis with SMA and Bollinger Bands')
plt.xlabel('Index')
plt.ylabel('Price')
plt.grid()
plt.show()

# Save the processed data to a new CSV
df.to_csv("processed_data_no_talib.csv", index=False)

# Print the first few rows to verify
print(df.head())