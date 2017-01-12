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

## 使用

```shell
$ python3 setup.py --help
Usage: setup.py <URL> [-w workfile] [options]

Options:
  -h, --help            show this help message and exit
  -d WEBDRIVER, --webdriver=WEBDRIVER
                        Web Driver
  --chrome-driver-path=CHROMEDRIVERPATH
                        Chromedriver path

  Other options:
    Caution: These options usually use default values.

    -w WORKFILE, --work-file=WORKFILE
                        Work file path
    --sim-threshold=THRESHOLD
                        Similarity threshold
    --min-children-count=MINCHILDRENCOUNT
                        Min children count of a DOM
    --min-children-deep=MINDEEP
                        Minimum deep of children of a DOM
    --min-similar-count=MINSIMILAR
                        Minimum count of a set of similar DOMs
Usage: setup.py <URL> [-w workfile] [options]
```

用法举例：

```shell
$ python3 'http://your-web-site.com' -w your_workfile.py -d chrome
```

其中`-w`默认为`./work.py`，这个脚本会插入到程序中执行，里面有几个变量，在[`/work.py`](https://github.com/sekaiamber/content-base-crawler/blob/master/work.py)列举了他们。具体各种例子可以看`/examples`内的多个例子。

其他参数请看[`/setup.py::Config`](https://github.com/sekaiamber/content-base-crawler/blob/master/setup.py#L21)中的`parser_system_options`和`parser_options`两个参数列表。

## 原理

本方案所有原理均写在[`/doc/doc.md`](https://github.com/sekaiamber/content-base-crawler/blob/master/doc/doc.md)中，十分详细，大家可以参考一下。

## LICENSE

CC-BY-NC-SA 3.0
