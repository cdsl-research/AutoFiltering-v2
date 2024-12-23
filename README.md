# AutoFiltering-v2
このソフトウェアは　CMDB-Createrの結果から重みをつけた後，通知されたアラートを分類し，アラートをまとめるソフトウェアです．
監視ソフトウェアはPrometheusとAlertManagerを想定しています．

https://github.com/cdsl-research/CMDB-Creater

### 環境
- Ubuntu 24.04.1 LTS

- Python 3.10.12

必要なライブラリ
Flask
slackweb
subprocess
yaml
prometheus_api_client
datetime



### 対象ソフトウェア

- Prometheus
- AlertManager

### 通知デバイス
Slack
以下の設定を事前に済ませといてください．
https://api.slack.com/messaging/webhooks


###　構成要素

- ```cmdb_data_get.py```
  - fetch_network_status(): cmdbに接続後要素を抽出
- ```weight.py```
  - monitoring_weight(): fetch_network_status()のデータから計算値を抽出
  - weight_calculation():計算値から重みを算出

 ### 使い方

cdで対象のディレクトリに移動
```
$ cd AutoFiltering-v2/notice
```

```
$ python3 notice.py 
```


以下のような表示が出ればOKです．

<img width="838" alt="スクリーンショット 2024-12-19 14 52 44" src="https://github.com/user-attachments/assets/b9b818f6-0275-43e0-ad55-3045791c297d" />




また通知されたアラートは以下のようになります．
<img width="1094" alt="スクリーンショット 2024-12-19 9 16 03" src="https://github.com/user-attachments/assets/8da6a9fc-86cb-49aa-9b4b-20d799028b13" />




 ###　最後に
 このソフトウェアはAlertManagerと組み合わせて使うことで障害発生箇所に絞ったアラート通知ができます．
ぜひ使ってみてください．
