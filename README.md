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

📌（以下截图来自`1.0`版本，后续已将维度范围改为`1~5`）

演示部分我的标注文件只有5个样本，需将所有的标注样本放到同一个文件夹中

![demo-data](https://foruda.gitee.com/images/1673409306632071575/2e501120_5117261.png "测试文件夹.png")

之后运行`Ding-Tag`标注工具，首次运行需要进行配置，主要配置标注人的身份，选择样本所在的文件夹以及最后标注文件`result.csv`的存储目录

![config-window](https://foruda.gitee.com/images/1673409440036613941/d806151a_5117261.png "配置界面.png")

以上三项为必填项，姓名需手动输入，文件夹的选择可以点击文件夹图标后进行选择，如果任意一项为空便确定，工具会进行提示

![config-tips](https://foruda.gitee.com/images/1673409574103369369/55b2720c_5117261.png "配置提示.png")

演示部分我选择以上所展示的音乐文件夹下的`data`文件夹

![my-config](https://foruda.gitee.com/images/1673409658258298982/a7f106f8_5117261.png "我的配置项.png")

点击确定后，即可进入软件主窗口

![mainwindow](https://foruda.gitee.com/images/1673409742675629607/3c783d41_5117261.png "播放完成的主界面.png")

主界面展示了当前标注的音频文件为`1.mp3`，通过左下方两个按键可进行`音频重播`与`播放/暂停`的控制，左侧展示了标注人员的身份，以及音频可能存在的问题选项和音频文件所需的标注项。当音频文件正常时，我们完成标注，点击提交，需要进行确定

![ok](https://foruda.gitee.com/images/1673409951169408566/cc4a08e0_5117261.png "提交确定框.png")

点击确定后自动进入下一个样本的标注，如果音频正常，无软件所展示的问题，则标注项全部为必填项，如果为空，软件将对用户进行提示

![tips](https://foruda.gitee.com/images/1673410065565155475/6f2beffc_5117261.png "音频无异常必须填写.png")

如果勾选具体异常后，标注项则可以不填，保持为空进行提交

![error-submit](https://foruda.gitee.com/images/1673410132263004688/b135f400_5117261.png "异常音频直接提交.png")

当所有样本未全部标注完成，用户退出了软件，之后再打开软件可以继续进行上次为完成的标注，而无需重头开始

![contuine](https://foruda.gitee.com/images/1673410439923466615/9beea6fb_5117261.png "中途退出.png")

所有样本标注完成后提示用户退出软件，标注完成后再次打开软件也会进行提示

![over](https://foruda.gitee.com/images/1673410622971579824/a83aef25_5117261.png "完成.png")

可在自己配置的标注文件保存目录中看到`result.csv`文件，该文件存储所有的标注结果

## 现存小bug

+ 在标注完成后，如果再次打开软件，即使用户按正常提示退出程序后，`Python`仍会保持进程，并未完全退出

  ![bug0](https://foruda.gitee.com/images/1673410827943072534/ae128a9b_5117261.png "bug.png")

## 项目参考

+ 工具`logo`设计来源：[logo在线设计生成器 - 几秒钟内在线制作logo - Shopify Hatchful](https://www.shopify.com/zh/tools/logo-maker)
+ 界面图标来源：[iconfont-阿里巴巴矢量图标库](https://www.iconfont.cn/)
+ 项目目录结构参考：[【Pyside6】桌面应用--目录、代码结构设计（附案例）_pyside项目例程_会振刀的程序员的博客-CSDN博客](https://blog.csdn.net/l782060902/article/details/124755656)
+ 内置播放器代码参考：[PySide6教程——基于QMediaPlayer的简易音频播放 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/521028351)

