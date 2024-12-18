import mysql.connector

def fetch_network_status():
    """
    MySQLデータベースから `network_status` テーブルの全データを取得する関数。
    
    Returns:
        list[dict]: 取得したデータを辞書型のリストで返す。
    """
    # MySQL接続設定
    mysql_config = {
        "host": "monitoring-master-ml",  # Kubernetes service名
        "user": "devuser",              # ユーザー名
        "password": "devuser",          # パスワード
        "port": 32000,                  # NodePort番号
        "database": "cmdb"              # データベース名
    }

    # データ取得用クエリ
    query = "SELECT * FROM network_status;"

    try:
        # MySQLに接続
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor(dictionary=True)  # 結果を辞書型で取得

        # クエリ実行
        cursor.execute(query)
        results = cursor.fetchall()

        return results  # 辞書型のリストを返す

    except mysql.connector.Error as e:
        # エラー時にはエラーメッセージを出力して空リストを返す
        print(f"MySQL Error: {e}")
        return []

    finally:
        # リソースのクリーンアップ
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()


# 関数を呼び出してデータを取得
data = fetch_network_status()

# データの確認
print(data)
