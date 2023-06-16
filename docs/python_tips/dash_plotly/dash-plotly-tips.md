# dash-plotly-tips

plotly-dashのtipsをまとめてます。

[Topに戻る](../../index.md)

## Dash Plotlyについて

データ分析について調べるとPythonでPlotly社が提供しているオープンソースのライブラリが公開されており、グラフ作成向けのライブラリであるPlotlyとデータ可視化用のWebアプリを作るためのライブラリ(フレームワーク)であるDashを使用することで、データの抽出から可視化をセットにしたダッシュボードを作成できる。

Dash公式ページには[User Guide](https://dash.plotly.com/)があり、Dash Callbacksまで読めばインタラクティブなダッシュボードを作成することができます。また、[Plotly Commnity Forum](https://community.plotly.com/)には運営やユーザーから仕様に関する情報が投稿されており、疑問点や不明点についても共有されています。

### 事例

【Python】Dashを使用してPlotlyのDatasetsをDownloadするWebアプリについて

[https://7rikazhexde-techlog.hatenablog.com/entry/2023/01/08/222513](https://7rikazhexde-techlog.hatenablog.com/entry/2023/01/08/222513)

### Dash Dev Tools

開発ツール

- [Dash Dev Toolsの公式ページ](https://dash.plotly.com/devtools)

#### Dash Dev Toolsの表示をオフにする方法

dev_tools_uiをFalseにする。

```
app.run(debug=True, dev_tools_ui=False)
```
