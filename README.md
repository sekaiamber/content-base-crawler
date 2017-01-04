# content-base-crawler
某种基于内容相似度的爬虫实现，这种方式暂时没有能确保是否可能，这个项目也是一个探索项目，我使用Python是因为Python写起来方便一点，但是注意：**若使用PhantomJS作为Webdriver，强烈建议使用JS开发，Python通过Selenium来通信PhantomJS，有性能问题**

## 开发

**我用Python3我自豪**

```shell
$ pip3 install selenium
$ pip3 install ansicolors
```

### 使用PhantomJS作为Webdriver（默认）

Mac下，建议使用`homebrew`安装`PhantomJS`。

```shell
$ brew install phantomjs
```

其他系统，如果自己去官网下的话，请设置好PATH。

### 使用Chrome driver作为Webdriver（`-m chrome`）

从[Google官网](https://sites.google.com/a/chromium.org/chromedriver/downloads)下载最新的Chromedriver，使用`--chrome-driver-path`设置路径，默认路径是`./chromedriver`。

