import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルからデータを読み込む
df = pd.read_csv('Japan-2022.csv', index_col=0)
print(df)
# 棒グラフを作成する
fig, ax = plt.subplots( )
df.plot(kind='barh', ax=ax, stacked=True,color={ 'blue', 'red'})

# グラフのタイトル、軸ラベルを設定する
ax.set_title('Population by Age and Gender')
ax.set_xlabel('Population')
ax.set_ylabel('Age')

# x軸の目盛りを設定する
xticks = range(0, 6000000, 1000000)
ax.set_xticks(xticks)
ax.set_xticklabels([f'{x//1000000}M' for x in xticks])

# グラフを表示する
if None :
    pass
plt.show()
