/*


str.center(width)  # strをwidthの幅で{中央寄せする}　-> 文字列
fillchar  # パディング文字
//math.log(x)  # x(数)の対数
//math.pi  # 円周率
//a[0]  # aの先頭 -> a

f(1, 1.0, a, "\n", '\\')  # 1と1.0とaと"\n"と'\\'

a % 2 != 0   # a(整数)が{奇数かどうか}
a % 2 == 1   # a(整数)が奇数かどうか
a % n == 0   # a(整数)がnの倍数かどうか
y == 0     # y(整数)が0かどうか
str(x)   # xの文字列表現

*/

len(a)  # aの{長さ|要素数|サイズ}
max(a, b)  # aとbの{最大値|大きい値|大きい方}
math.pi  # 円周率
a % 2 == 0   # a(整数)が{偶数かどうか}

print()  # 空行を{出力する|表示する} ->
print(a)  # aを{出力する|表示する} ->
print(a, b)  # aとbを順に{出力する|表示する} ->

end = ''  # 改行なしで
end = x  # xを終端記号{に用いて|として}
sep = ''  # 区切りなしで
sep = x  # xを[区切り|区切り記号|セパレータ]{に用いて|として}
file = x  # xを出力先{に用いて|として}
flush = True  # [バッファを|]フラッシュしながら

open(file)  # file(ファイル名)を{開く} -> ファイル
open(file, 'w')  # file(ファイル名)を書き込みモードで{開く} -> ファイル
encoding = x  # x(エンコーディング)を用いて

s.startswith(x)  # s(文字列)がx(接頭辞)で始まるかどうか
s.replace(old, new)  # s(文字列)のold(文字列)をnew(文字列)で{置換する|置き換える} -> 文字列
s.replace(x, '')  # s(文字列)からx(文字列)を全て{取り除く} -> 文字列

/*
pd.read_csv(file) # file(CSVファイル)から[データを|]{読む} -> データフレーム
*/

pd.read_csv(file) # {read} data frame from file(CSV file) -> data frame

