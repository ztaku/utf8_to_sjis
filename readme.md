# UTF-8をsjijsに変換する。

## 以下のバイナリファイルを作成する。

utfバイト列(1-3バイト), sjis 2バイト



## utfは1byte目で、バイト数が決まる。



| データ      | 長さ                         |
| ----------- | ---------------------------- |
| 00-7f       | 1バイト文字                  |
| 8x,9x,Ax,Bx | 多バイト文字の２バイト目以降 |
| Cx,Dx       | 2バイト文字の開始バイト      |
| EX          | 3バイト文字の開始バイト      |





