def add_technical_indicators(data):
    """
    Додава технички индикатори на податоците.

    :param data: Pandas DataFrame со обработени податоци.
    :return: DataFrame со додадени индикатори.
    """
    # Додавање на SMA (5-дневен)
    data['SMA_5'] = data['last_transaction_price'].rolling(window=5).mean()

    # Додавање на EMA (5-дневен)
    data['EMA_5'] = data['last_transaction_price'].ewm(span=5, adjust=False).mean()

    # Додавање примерни сигнали (логиката може да биде посложена)
    data['Signal'] = 'Hold'
    data.loc[data['last_transaction_price'] > data['SMA_5'], 'Signal'] = 'Buy'
    data.loc[data['last_transaction_price'] < data['EMA_5'], 'Signal'] = 'Sell'

    return data
