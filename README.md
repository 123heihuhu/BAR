# 设计一带一路数据表（bar/BaR）
文件在world_BaR里
## 导出模式

将表bar加入至world数据库中，利用mysqldump命令一并导出

## 原始数据

|文件名|内容|
|-----|----|
|iso3166-1-obor.xlsx|标准化文件|
|RAW_DATA_INPUT.xlsx|bar表输入数据与更改|
|sql_for_gpp.csv|UN给出的以地区、年为细分的GDP数据|

## 优化想法

world数据库的内容需要更新，但是world数据库的外键设置，使得在更改原始<父数据>很棘手，导致bar表的国家名与country表的国家名略微不统一 ***常常会引起由外键设置的报错***
