import pandas as pd
import json

class read:
    def dataframe(): #  CSVファイル➡DataFrame
        # CSVファイルを読み込む
        df = pd.read_csv('data.csv')
        (df.columns)
        (df[df.Region =='Japan'])
        """
            Index Region    Year  0-1  0-4  0-14  0-17  0-19  0-24  ... 25-69   50+   60+   65+   70+   75+   80+  85+  90+     
        7825   7826  Japan  2022.0  1.3  3.4  11.6  14.3  16.1  20.9  ...  55.2  49.6  35.8  29.9  23.9  16.3  10.5  5.7  2.4     
        7826   7827  Japan  2023.0  1.3  3.3  11.5  14.1  15.9  20.7  ...  55.1  50.2  36.1  30.1  24.2    17  10.8  5.9  2.5     
        """
        # DataFrameをJSON形式に変換する
        json_data = df.to_json(orient='records')

        (json_data)
        df_read = pd.read_json(json_data)
        (df_read)

        """
            Index                     Region    Year  0-1  0-4  ...   70+   75+  80+  85+  90+   
        0          1                      WORLD  2022.0  3.3  8.3  ...   6.3   3.6    2  0.9  0.3   
        1          2                      WORLD  2023.0  3.3  8.2  ...   6.4   3.7    2  0.9  0.3   
        2          3                      WORLD  2024.0  3.3  8.1  ...   6.6   3.8    2  0.9  0.3   
        """

    def write():
        import csv
        import json

        # CSVファイルの読み込み
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # JSONファイルへの書き込み
        with open('data.json', 'w') as f:
            json.dump(rows, f)

    def jyson():
        import json

        # JSONファイルを読み込む
        with open('data.json', 'r') as f:
            data = json.load(f)

        # 条件に一致する要素を抽出する
        result = [item for item in data if item.get('location') == 'Japan' and item['year'] == '1950' ]

        result = []
        for item in data:
            if item['location'] == 'Japan' and item['year'] == '1950' :
                item['male'] = float(item['male'])
                item['female'] = float(item['female'])
                item['total'] = float(item['total'])
                result.append(item)

        # JSONファイルへの書き込み
        with open('location_year.json', 'w') as f:
            json.dump(result, f)

class Json_hash: #  JSONデータを連想配列に変換、JSファイルに書き込む
    def read():
        # JSONファイルを読み込む
        with open('data.json', 'r') as f:
            data = json.load(f)
        data = data#[:1000]

        Json_hash.dd(data,{},{})

    def dd(data, dd, d): # 二次元辞書を作成
        for dct in data:
            K = dct['location']
            k = dct['year']
            dd = {**dd,**{K:{}}}
            d = {**d,**{k:[]}}
            dd[K].update(**d)

        for dct in data:
            dct = Json_hash.str_int(dct) # 整数に変換

            K = dct['location']
            k = dct['year']
            dd[K][k].append(dct)
            (dd[K][k])
        Json_hash.write(dd)

    def write(dd):
        # JSファイルへの書き込み
        with open('hash.js', 'w') as f:
            json.dump(dd, f)

    def str_int(dct): # 整数に変換
        dct['male'] = int(float(dct['male'])*1000)
        dct['female'] = int(float(dct['female'])*1000)
        dct['total'] = int(float(dct['total'])*1000)
        return dct

if __name__ == '__main__':   
    pass
    Json_hash.read()
