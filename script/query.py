import mysql.connector
class Query:
     def get_tabele_name():
        #データベースへの接続
        conn = mysql.connector.connect(
        host="localhost",
        user="root", #
        password="mysql", #
        database="total"  #
        )

        """
        MySQLなどのデータベースを操作するときには、Pythonでは一般的に「カーソル」オブジェクトを使用します。カーソルはデータベース接続の一部で、SQLクエリを実行したり結果を取得したりするための主要なインターフェースを提供します。

        カーソルは基本的に、SQLクエリの結果を指し示す「ポインタ」のようなものです。SQLクエリを実行した後、カーソルは結果セット（行の集合）を指し示します。そして、カーソルを使って結果セット内の行を一つずつ（または複数行ずつ）取得することができます。"""

        #カーソルを生成
        cursor = conn.cursor()
        
        # クエリを実行します
        cursor.execute("SHOW TABLES")

        #テーブルの一覧
        l = []
        for tx, in cursor:
            l.append(tx)
        (l) # ['afghanistan', 'africa', 'albania', 'algeria',

        # カーソルを閉じます
        cursor.close()

        # データベース接続を閉じます
        conn.close()

if __name__ == '__main__':  
    Query.get_tabele_name()

    if None != None:
        pass