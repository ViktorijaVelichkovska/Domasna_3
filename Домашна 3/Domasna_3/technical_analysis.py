import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('combined_data.csv')


df['last_transaction_price'] = df['last_transaction_price'].replace({',': '.'}, regex=True)  # Замени запирки со точки
df['last_transaction_price'] = df['last_transaction_price'].replace({'\\.' : ''}, regex=True)  # Отстрани точките за илјадници
df['last_transaction_price'] = df['last_transaction_price'].astype(float)  # Конвертирај во float


print(df.head())


df['SMA_14'] = df['last_transaction_price'].rolling(window=14).mean()


df['EMA_14'] = df['last_transaction_price'].ewm(span=14, adjust=False).mean()

delta = df['last_transaction_price'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()

rs = gain / loss
df['RSI_14'] = 100 - (100 / (1 + rs))


ema_12 = df['last_transaction_price'].ewm(span=12, adjust=False).mean()
ema_26 = df['last_transaction_price'].ewm(span=26, adjust=False).mean()
df['MACD'] = ema_12 - ema_26
df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()


df['BB_upper'] = df['SMA_14'] + (df['last_transaction_price'].rolling(window=14).std() * 2)
df['BB_lower'] = df['SMA_14'] - (df['last_transaction_price'].rolling(window=14).std() * 2)

def generate_signals(row):
    if row['last_transaction_price'] > row['BB_upper']:
        return 'Sell'
    elif row['last_transaction_price'] < row['BB_lower']:
        return 'Buy'
    else:
        return 'Hold'

df['Signal'] = df.apply(generate_signals, axis=1)


print(df[['date', 'last_transaction_price', 'SMA_14', 'EMA_14', 'RSI_14', 'MACD', 'Signal_Line', 'BB_upper', 'BB_lower', 'Signal']])

df.to_csv('technical_analysis_results.csv', index=False)


plt.figure(figsize=(12, 6))
plt.plot(df['last_transaction_price'], label='Last Transaction Price', color='blue')
plt.plot(df['SMA_14'], label='SMA 14', color='orange')
plt.fill_between(range(len(df)), df['BB_upper'], df['BB_lower'], color='gray', alpha=0.2, label='Bollinger Bands')
plt.legend(loc='best')
plt.title('Stock Analysis with SMA and Bollinger Bands')
plt.xlabel('Index')
plt.ylabel('Price')
plt.grid()


plt.savefig('technical_analysis_plot.png')


plt.close()


df.to_csv('technical_analysis_results.csv', index=False)


print(df.head())
