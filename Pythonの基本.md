# Pythonの基本

## Pythonの2つの動かし方

- インタラクティブモード
  - ユーザに文を入力してもらい、逐次実行しながら行う
    - IDLE：インタラクティブモードのコンソール
- ファイル実行
  - Pythonのスクリプトをテキストファイルに書いて、コマンド実行

## 値のキャスト

- 整数にキャスト

  ```python
  int(値)
  ```

- 実数にキャスト

  ```python
  float(値)
  ```

- テキストにキャスト

  ```python
  str(値)
  ```

- 真偽値にキャスト

  ```python
  bool(値)
  ```

## if分の書き方

- インデントの位置重要

  ```python
  if 条件:
    ・・・条件がTrueのときの処理・・・・
  ```

  ```python
  if 条件:
    ・・・条件がTrueのときの処理・・・・
  else:
    ・・・条件がFalseのときの処理・・・
  ```

  ```python
  if 条件1:
    ・・・実行する処理・・・・
  elif 条件2:
    ・・・実行する処理・・・・
  else:
    ・・・それ以外の場合の処理・・・・
  ```

## 繰り返し「while」

  ```python
  while 条件:
    ・・・繰り返す処理・・・
  ```

## 多数の値を保管する「リスト(list)」

リストは、番号で値を管理する
**ミュータブル** (後で値変更を行うことが可能)

- リストを作る（１）

    ```python
    [値1, 値2, 値3, ・・・]
    ```

- リストを作る（２）

    ```python
    list(値1, 値2, 値3, ・・・)
    ```

- リストを値に代入する

    ```python
    変数 = リスト
    ```

- リストから値を取り出す

    ```python
    リスト[番号]
    ```

- リストに値を保管する

    ```python
    リスト[番号] = 値
    ```

## リストと繰り返し構文「for」

```python
for 変数 in リスト:
  ・・・実行する処理・・・
```

## 値を変更できない「タプル(tuple)」

作った後で、値を変更できない
**イミュータブル** (後で値を変更できない)

- タプルを作る（１）

  ```python
  (値1, 値2, 値3, ・・・)
  ```

- タプルを作る（２）

  ```python
  tuple(値1, 値2, 値3, ・・・)
  ```

- タプルの足し算

  ```python
  タプル + タプル
  ```

- タプルの掛け算

  ```python
  タプル * 整数
  ```

## 連続する数列を扱う「レンジ(range)」

多数の値をまとめて扱い、かつ**イミュータブル**
**連続する数列**を扱うためのもの

- レンジを作る（１）

  ```python
  range(数字)
  ```

- レンジを作る（２）
※ 指定した数値 **「未満」** の数列を作る

  ```python
  range(開始値, 終了値)
  ```

- レンジを作る（３）
※ 指定した数値 **「未満」** の数列を作る

  ```python
  range(開始値, 終了値, 間隔)
  ```

## 名前で値を管理する「辞書(dict)」

- 辞書を作る（１）

  ```python
  {キー1: 値１,キー2: 値２,・・・・・}
  ```

- 辞書を作る（２）

  ```python
  dict(キー1 = 値１,キー2 = 値２,・・・・・)
  ```

## 辞書とfor文

```python
for 変数 in 辞書:
  ・・・辞書[変数]から値を取り出し処理・・・
```

## 関数

- input関数
  - [python_input.py](./basic/python_input.py)

    ```bash
    # open terminal
    python python_sample.py 
    ```

- モジュールと関数
  - モジュールを組み込む（１）

    ```python
    import モジュール
    ```

  - モジュールを組み込む（２）

    ```python
    import モジュール import 関数など
    ```

- fsum関数
  - [python_fsum.py](./basic/python_fsum.py)

      ```python
      # open terminal
      python python_fsum.py
      ```

- 自作関数
  - defという予約後の後に関数の名前を指定

    ```python
    def 関数名(引数):
      ・・・実行する処理名・・・
    ```

  - [python_def.py](./basic/python_def.py)

    ```python
    # open terminal
    python python_def.py
    ```

## クラスを作る

- クラスの作り方（１）

  ```python
  class クラス名
    ・・・クラスの内容・・・
  ```

- インスタンス作成

  ```python
  変数 = クラス()
  ```

  - [python_class.py](./basic/python_class.py)

    ```python
    # open terminal
    python python_class.py 
    ```

- 初期化メソッド

  ```python
  def __init__(self):
    ・・・処理・・・
  ```

  - 初期化メソッド
  [python_def_init.py](./basic/python_def_init.py)

    ```python
    # open terminal
    python python_def_init.py
    ```

  - 名前つき引数

    ```python
    # python_def_init.pyの6行目以降を変更
      def __init__(self, name='noname', age=0, mail='noaddress'):
          self.name = name
          self.age = age
          self.mail = mail
    ```

## 継承

- クラスの作り方（２）

  ```python
  class クラス名 (継承するクラス):
    ・・・クラスの内容・・・
  ```

  - [python_inheritance.py](./basic/python_inheritance.py)

    ```python
    # open terminal
    python python_inheritance.py
    ```

## クラスメソッド

- クラスから直接呼び出して実行できるメソッド

  ```python
  # @classmethod:アノーテーション
  @classmethod
  #cls:クラス自身を表す
  def メソッド名(cls):
    ・・・処理・・・
  ```

  - [python_python_classmethod.py](./basic/python_python_classmethod.py )

    ```python
    # open terminal
    python python_python_classmethod.py 
    ```
