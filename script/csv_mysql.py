import pandas as pd
from sqlalchemy import create_engine
class total:
    def csv_sql():
       # CSVファイルを読み込む
       df = pd.read_csv('data.csv')
       # male, female, totalの値を1000倍して整数に変換する
       df['male'] = (df['male'] * 1000).astype(int)
       df['female'] = (df['female'] * 1000).astype(int)
       df['total'] = (df['total'] * 1000).astype(int)
       """
       [mysql]
       host=localhost
       database=json
       user=root
       password=mysql
       """
       # MySQLの接続設定を作成
       database_username = 'root'
       database_password = 'mysql'
       database_ip       = 'localhost'
       database_name     = 'un'
       database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                 format(database_username, database_password, 
                                                        database_ip, database_name))

       # DataFrameをSQLに書き込む
       df.to_sql(con=database_connection, name='location_age', if_exists='append')

class splits: # 分割
    def df_(d):
       # CSVファイルを読み込む
       df = pd.read_csv('data.csv')
       # male, female, totalの値を1000倍して整数に変換する
       df['male'] = (df['male'] * 1000).astype(int)
       df['female'] = (df['female'] * 1000).astype(int)
       df['total'] = (df['total'] * 1000).astype(int)
       df = df.query('location == "World" and year == "2023"')
       print(df)
       splits.conn(d,df)### 
    
    def conn(d,df):
       # MySQLの接続設定を作成
       database_username = 'root'
       database_password = 'mysql'
       database_ip       = 'localhost'
       database_name     = d.get('database_name')
       database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                 format(database_username, database_password, 
                                                        database_ip, database_name))
       splits.sql(d, df, database_connection)

    def sql(d, df, database_connection):
       # DataFrameをSQLに書き込む
       df.to_sql(con=database_connection, name= d.get('name'), if_exists='append')

class lymft:
    def csv_sql():
        # CSVファイルを読み込む,lymft
        df = pd.read_csv('./data/data.csv')
        
        # カラム「location」ごとに分割してテーブルを作成
        for location, location_df in df.groupby('location'):
            # カラム「year」ごとに分割してテーブルを作成
            # カラム「year」ごとに分割してテーブルを作成
            for year, year_df in location_df.groupby('year'):
                year_df_copy = year_df.copy()
                year_df_copy['male'] = (year_df['male'] * 1000).astype(int)
                year_df_copy['female'] = (year_df['female'] * 1000).astype(int)
                year_df_copy['total'] = (year_df['total'] * 1000).astype(int)
                
                """
                [mysql]
                host=localhost
                database=json
                user=root
                password=mysql
                """
                # MySQLの接続設定を作成
                database_username = 'root'
                database_password = 'mysql'
                database_ip = 'localhost'
                database_name = 'test'
                table_name = f'{location}_{year}'
                database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                    format(database_username, database_password, 
                                                            database_ip, database_name))

                # DataFrameをSQLに書き込む
                year_df_copy.to_sql(con=database_connection, name=table_name, if_exists='append')

class total:
    def csv_sql():
        # CSVファイルを読み込む,lymft
        df = pd.read_csv('./data/total.csv')
        
        # カラム「location」ごとに分割してテーブルを作成
        for location, location_df in df.groupby('location'):
                # DataFrameをコピーしてから操作を行う
                location_df_copy = location_df.copy()
                location_df_copy['male'] = (location_df['male'] * 1000).astype(int)
                location_df_copy['female'] = (location_df['female'] * 1000).astype(int)
                location_df_copy['total'] = (location_df['total'] * 1000).astype(int)
                
                """
                [mysql]
                host=localhost
                database=json
                user=root
                password=mysql
                """
                # MySQLの接続設定を作成
                database_username = 'root'
                database_password = 'mysql'
                database_ip = 'localhost'
                database_name = 'total'
                table_name = f'{location}'
                database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                    format(database_username, database_password, 
                                                            database_ip, database_name))

                # DataFrameをSQLに書き込む
                location_df_copy.to_sql(con=database_connection, name=table_name, if_exists='append')

class age_group:
    def csv_sql():
        # CSVファイルを読み込む,lymft
        df = pd.read_csv('./data/medium.csv')
        
        # カラム「location」ごとに分割してテーブルを作成
        for location, location_df in df.groupby('location'):
                              
            # MySQLの接続設定を作成
            database_username = 'root'
            database_password = 'mysql'
            database_ip = 'localhost'
            database_name = 'medium'
            table_name = f'{location}'
            database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))

            # DataFrameをSQLに書き込む
            location_df.to_sql(con=database_connection, name=table_name, if_exists='append')


class abstraction: # 抽出, 捨象
    def cvs_df_column():
        df = pd.read_csv('./data/medium.csv')
        print(list(df['location']))
        d = {}
        for i in list(df['location']):
            d ={ **d,**{i:None}} 
        print(list(d.keys()))


if __name__ == '__main__':  
    abstraction.cvs_df_column()
    if None != None:
        age_group.csv_sql()
        total.csv_sql()
        lymft.csv_sql()

    # mysql> create database unsd;
    # mysql> use unsd;
    d = {'database_name':'unsd', 'name':'location_age'} # 国連統計部（UNSD）
    splits.df_#(d)
    


    """
    error connecting: Error: ER_NOT_SUPPORTED_AUTH_MODE: 
    Client does not support authentication protocol requested by server; 
    consider upgrading MySQL client
    
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mysql';
    """

"""
「MySQLに書き込みできなかったため、変更した特殊文字と外国語」
-/()',.
curaçao,côte d'ivoire,réunion:,saint barthélemy,türkiye
"""