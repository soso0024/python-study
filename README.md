# python-study<!-- omit in toc -->
これはPythonの勉強用リポジトリです。

今回は、pythonでのデータ分析を学習していきます。  
記載しているプログラムは、CSVファイルから特定の条件を満たす行を抽出して、新しいCSVファイルに保存するプログラムです。

また、不要なcsvファイルの列を削除するプログラムも記載しています。

## 目次<!-- omit in toc -->
- [最後に一言](#最後に一言)

## プログラムの概要
1. 比較する比較するCSVファイルの数を定義する。
2. CSVファイルのパスを取得するため、各ファイルのプレフィックス、サフィックスを指定し、ループでパスを生成する
3. 抽出したデータを保存する新しいCSVファイルのパスを定義する。
4. SPSの列のインデックスを取得するため、最初のファイルを読み込み、ヘッダー行を取得して、SPSの列のインデックスを取得する。
5. セルA、B列が一致している行を抽出するため、最初のファイルを読み込み、ヘッダー行を取得して、各行を読み取り、インスタンスタイプと可用性ゾーンを取得する。
6. 各ファイルをループし、A、B列が一致している行を探し、SPSの値を取得する。
7. 抽出したデータを新しいCSVファイルとして保存する。

このプログラムでは、比較するCSVファイルの数が非常に多いため、ファイルパスの生成にループを使用しています。また、CSVファイルの読み込みにはcsvライブラリを使用しています。

# 最後に一言
努力します！💪