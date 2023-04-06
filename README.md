![Ding-Tag](https://foruda.gitee.com/images/1673408850565785700/1d0edf23_5117261.png "logo.png")

# Ding-Tag

## 项目简介

`Ding-Tag` 是为了完成音频数据的一些标注工作，使用`PySide6` 制作的一个标注工具，主要对音频的”文本、角色、离散情感标签、愉悦维、激活维“进行标注。

## 项目使用

如果直接使用项目源代码，还需安装`Python`解释器，然后再安装项目所需的依赖，最后运行即可

```shell
git clone https://gitee.com/byack/ding-tag.git
cd ding-tag
pip install -r requirement.txt
python app.py
```

也可以到[发布页面](https://gitee.com/byack/ding-tag/releases)下载打包好的程序，直接解压运行`app.exe`文件即可

## 项目演示

演示部分我的标注文件只有10个样本，需将所有的标注样本放到同一个文件夹中

![](https://foruda.gitee.com/images/1680781957738275582/e8edef34_5117261.png "屏幕截图")

之后运行`Ding-Tag`标注工具，首次运行需要进行配置，主要配置标注人的身份，选择样本所在的文件夹、标注结果文件的存储目录，如果需要使用百度的语音识别服务，还需要配置官方的KEY

![](https://foruda.gitee.com/images/1680782001586293917/df6e92a2_5117261.png "1-配置.png")

以上三项为必填项，不然程序会提示报错，语音识别服务为可选项，确定之后进入主界面开始标注

![](https://foruda.gitee.com/images/1680782141674387570/323384e0_5117261.png "主界面标注.png")

标注完成后点击提交即可，之后需要手动进行确认

![](https://foruda.gitee.com/images/1680782188237509721/acc6b793_5117261.png "3-提交确定.png")

其提交的结果会进行一些合规性检查，如果不合规，软件会弹窗提示，以下是一些不合规情况

![](https://foruda.gitee.com/images/1680782273812196679/3c147426_5117261.png "4-不能为空.png")

![](https://foruda.gitee.com/images/1680782297414920660/19a38660_5117261.png "5-用户不标.png")

![](https://foruda.gitee.com/images/1680782321628563442/37add187_5117261.png "6-只标一个.png")

![](https://foruda.gitee.com/images/1680782340370668371/d2577cab_5117261.png "7-时长异常冲突.png")

正常标注完成后，软件会提示关闭程序

![](https://foruda.gitee.com/images/1680782386824652406/55e9b573_5117261.png "8-标注完成.png")

其所有标注结果都在初始配置的”标注文件存储路径“中

![](https://foruda.gitee.com/images/1680782453514952850/01061a94_5117261.png "屏幕截图")

## 现存小bug

+ 在标注完成后，如果再次打开软件，即使用户按正常提示退出程序后，`Python`仍会保持进程，并未完全退出

  ![bug0](https://foruda.gitee.com/images/1673410827943072534/ae128a9b_5117261.png "bug.png")
  
+ 标注完一个样本进入下一个样本，如果立马关闭窗口，其语音识别子进程已经启动，可能还没有识别完成，此时快速退出，后台可能会残留一个子进程

## 项目参考

+ 工具`logo`设计来源：[logo在线设计生成器 - 几秒钟内在线制作logo - Shopify Hatchful](https://www.shopify.com/zh/tools/logo-maker)
+ 界面图标来源：[iconfont-阿里巴巴矢量图标库](https://www.iconfont.cn/)
+ 项目目录结构参考：[【Pyside6】桌面应用--目录、代码结构设计（附案例）_pyside项目例程_会振刀的程序员的博客-CSDN博客](https://blog.csdn.net/l782060902/article/details/124755656)
+ 内置播放器代码参考：[PySide6教程——基于QMediaPlayer的简易音频播放 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/521028351)

