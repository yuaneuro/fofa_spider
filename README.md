# FOFA_Spider



本脚本采用python3开发，使用selenium和chrome爬取，Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。所以爬取的时候无需api_key，所以理论来说你能从网页上能查询到多少数据就能爬取多少数据。

## 依赖安装

```bash
pip install selenium 
```

## 使用说明

- 首先需要配置selenium和Chromedriver，在https://npm.taobao.org/mirrors/chromedriver/ 网站上下载和浏览器和系统匹配的版本，然后将其解压到环境目录下，或本脚本目录下

- 运行`python get_cookes.py`，然后在打开的浏览器上输入账号和密码登录，登录后会自动把cookie保存在`cookies.txt`中，方便我们爬取，当然你也可以将其他账户的cookie放在`cookies.txt`中。

- 然后运行以下命令

```bash
python fofaspider.py 需要搜索的命令 需要爬取的页数
```

例如：

```bash
python fofaspider.py 'app="APACHE-Shiro"' 200
```


程序会将爬取的内容保存在result文件夹中，并以日期和时间为后缀方便区分



