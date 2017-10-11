## Introduction
友達に相談された時や誰かを慰めてあげたいとき、
**「何か。。何かカッコイイことを言いたい!。。」**という需要に答えるアプリです。

## Install
1. Python(2.7) をインストールします。
1. pipを入れます。
1. `pip install -r requirements.txt` と実行し、必要なパッケージをインストールします。
1. 環境変数TEXTKEYとTYPOKEYを設定します。
TEXTKEYにはA3RTのText Suggest APIのAPI Keyを設定します。
TYPOKEYにはProofreading APIのAPI Keyを設定します。
`export TEXTKEY="eUHenNG~~~~"`
`export TYPOKEY="ejNnEAe~~~~"`
1. インストール完了です。How to Useに進んでください。


## How to Use
#### ランダムにセリフを生成
1.  index.pyを実行します
ex. ```python index.py```
1. それっぽいセリフが出力されるのを確認します。
ex.  `酒は人生である。`
1.  それっぽい画像に重ねたら完成です。
![sake](https://github.com/frnfnts/recruit_A3RT_hack/blob/images/images/sake.jpg?raw=true)


#### 主語を指定してセリフを生成
1. セリフの最初に来る適当な単語を引数で渡して実行します。
ex. ```python index.py 幸せ```
1. それっぽいセリフが出力されるのを確認します。
ex.  `幸せは人生であると思っている。`
1.  おじいちゃんに言わせたら完成です。
![sake](https://raw.githubusercontent.com/frnfnts/recruit_A3RT_hack/images/images/ojiichan.jpg)

