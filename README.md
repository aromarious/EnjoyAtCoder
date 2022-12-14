# AtCoder でプログラミング学習

教えた記録は zenn で書く。
[aromarious さんの記事一覧 | Zenn](https://zenn.dev/aromarious)

---

## 【2022 年夏休み】

---

### 《**9/1 木**》『Python コードレシピ集』を渡す

指示：昨日解いた [ABC157A - Duplex Printing](https://atcoder.jp/contests/abc157/tasks/abc157_a) を別の解き方で解いてごらん。ヒント「切り上げ」

- 問題 [ABC157A - Duplex Printing](https://atcoder.jp/contests/abc157/tasks/abc157_a) → [📰 提出コード](/abc157/a/solve_abc157_a_another.py)

---

### 《**9/1 木**》『Python コードレシピ集』を渡す

道具一覧が載っているから、と[『Python コードレシピ集』](https://amzn.to/3wGJQlp)を渡した。自分で探す練習。

- 問題 [ABC088A - Infinite Coins](https://atcoder.jp/contests/abc088/tasks/abc088_a) → [📰 提出コード](/abc088/a/solve_abc088_a.py)
- 問題 [ABC157A - Duplex Printing](https://atcoder.jp/contests/abc157/tasks/abc157_a) → [📰 提出コード](/abc157/a/solve_abc157_a.py)

---

### 《**8/24 水**》独力でやれるようになってきた。2 問こなす

本人が解き筋を独力で考えて、それに応じた道具を渡すようになってきた。

- 問題 [ABC085A - Already 2018](https://atcoder.jp/contests/abc085/tasks/abc085_a) → [📰 提出コード](/abc085/a/solve_abc085_a.py)
- 問題 [ABC064A - RGB Cards](https://atcoder.jp/contests/abc064/tasks/abc064_a) → [📰 提出コード](/abc064/a/solve_abc064_a.py)

#### 🔧 渡した道具

- `string.split()`
- `int(string)`
- `string.replace(before, after)`
- `==`（比較演算子）

---

### 《**8/19 金**》 初めての B 問題。ABC069B - i18n 〜 `len(string), string[n], str(int)`

初めての B 問題に挑戦。✍🏻[ABC069B - i18n](https://atcoder.jp/contests/abc069/tasks/abc069_b)

#### 🔧 渡した道具

- `len(文字列)` 文字列の文字数を返す関数
- `文字列[n]` 文字列内 n 番目の文字を返す（最初の文字は 0 番目）
- `str(数)` 数を文字列に変換する

#### 📰 コード

- [提出した解答](/abc069/b/solve_abc069_b.py)

---

### 《**8/18 木**》 ABC095A - Something on It 〜 `str.count(substr)`

文字列のメソッドを使う。✍🏻[ABC095A - Something on It](https://atcoder.jp/contests/abc095/tasks/abc095_a)

#### 🔧 渡した道具

- `文字列.count(部分文字列)` 文字列の中に部分文字列が何回出現するか数える

#### 📰 コード

- [提出した解答](/abc095/a/solve_abc095_a.py)

---

### 《**8/17 水**》 ABC081A - Placing Marbles 〜 `for`文を使って

前回の説明をうけて、実際に問題を解くコードを書いた。✍🏻[ABC081A - Placing Marbles](https://atcoder.jp/contests/abc081/tasks/abc081_a) 2 回目

#### 🔧 渡した道具

今回は新しい道具は渡さなかったが、今まで使ってきたこと（変数宣言や代入など）の理解を深めた。

- 合計を保持する変数は`for`文の前で宣言する
- 代入文は方程式じゃない。解かない。（数学が得意な子のため数学の式と混同していた）
- 代入文の読み方は「右辺を計算する」「左辺の変数の内容を今計算した結果で上書きする」

#### 📰 記事とコード

- [中学生に AtCoder でプログラミングを教える記録 7 回目 〜 ABC081A - Placing Marbles を for 文を使って解く](https://zenn.dev/aromarious/articles/enjoy-atcoder-07)
- [提出した解答](/abc081/a/solve_abc081_a_using_for.py)

---

### 《**8/15 月**》 配列（list）と`for`文のレクチャー

Python の配列（list）について一通り教えたあと、配列の要素をひとつずつ処理する`for`文を教えた。

#### 🔧 渡した道具

- [2-2. リスト (list) — Python プログラミング入門 documentation](https://utokyo-ipp.github.io/2/2-2.html) 「理解だけすればいい、覚える必要はない」と前置きし、このページを見せながら口頭で説明した。
- `for`文を使って繰り返すことを教え、実際にコードを書いて実行してみせた

#### 📰 記事

- [中学生に AtCoder でプログラミングを教える記録 6 回目 〜 Python の list（配列）と for 文を教える](https://zenn.dev/aromarious/articles/enjoy-atcoder-06)

---

### 《**8/12 金**》 提出までの流れのおさらい ABC081A - Placing Marbles

前回の復習。[ABC081A - Placing Marbles](https://atcoder.jp/contests/abs/tasks/abc081_a)を使って、流れをおさらいする。

#### 📰 記事とコード

- [中学生に AtCoder でプログラミングを教える記録 5 回目 〜 ABC081A - Placing Marbles](https://zenn.dev/aromarious/articles/enjoy-atcoder-05)
- [提出した解答](/abc081/a/)

---

### 《**8/10 水**》 初めての提出。ABC086A - Product

初めて過去問を提出。`AC`をゲット。題材は ✍🏻 [ABC086A - Product](https://atcoder.jp/contests/abc086/tasks/abc086_a)

#### 🔧 渡した道具

- `*` , `%`
- `if`文

#### 📰 記事とコード

- [中学生に AtCoder でプログラミングを教える記録 3 回目 〜 初めての提出（前半）](https://zenn.dev/aromarious/articles/enjoy-atcoder-03)
- [中学生に AtCoder でプログラミングを教える記録 4 回目 〜 初めての提出（後半）](https://zenn.dev/aromarious/articles/enjoy-atcoder-04)
- [提出した解答](/abc086/a/)

---

### 《**8/4 木, 8/9 火**》 AtCoder の説明

本人に AtCoder 自体を説明。

- [中学生に AtCoder でプログラミングを教える記録 2 回目 〜 AtCoder 自体の説明](https://zenn.dev/aromarious/articles/enjoy-atcoder-02)

---

## 小学生時代と今回の環境構築

本人のスキル概要説明及び今回用の環境構築の記事

- [中学生に AtCoder でプログラミングを教える記録 1 回目 〜 背景と環境概要](https://zenn.dev/aromarious/articles/enjoy-atcoder-01)
