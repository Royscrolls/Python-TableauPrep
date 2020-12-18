import pandas as pd
import requests

def Get_Crypto_Data(df):
    URL="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=7d"
    response=requests.get(URL)
    data=response.json()
    df= pd.DataFrame.from_dict(data, orient='columns')

    df=df.drop(['image', 'fully_diluted_valuation','high_24h','low_24h','circulating_supply','max_supply','ath','ath_date','atl','atl_date','price_change_24h', 'market_cap_change_24h','roi','total_supply', 'ath_change_percentage','atl_change_percentage'], axis = 1) 
    return df

def get_output_schema():
    return pd.DataFrame({
            'id' : prep_string(),
            'symbol' :  prep_string(),
            'name' : prep_string(),
            'current_price' : prep_decimal(),
            'price_change_percentage_7d_in_currency' : prep_decimal(),
            'market_cap_change_percentage_24h' : prep_decimal(),
            'market_cap_rank' : prep_int(),
            'total_volume' : prep_decimal(),
            'last_updated' : prep_datetime(),


})