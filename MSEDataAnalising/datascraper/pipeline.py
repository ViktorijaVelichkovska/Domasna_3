from datascraper.filters import fil1, fil2, fil3


def process_data(input_data):
    # data = fil1(input_data)
    data = fil1(input_data)
    print(data)
    data = fil2(data)
    print(data)
    data = fil3(data)
    return data

if __name__ == "__main__":
    url = "https://www.mse.mk/mk/stats/symbolhistory/KMB"  
    url_corrected = "https://www.mse.mk/en/stats/current-schedule" 
    # data = process_data(url)  
    data = process_data(url)   

  

   
