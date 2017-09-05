sloth
=====

[![Build Status](https://travis-ci.org/cvhciKIT/sloth.svg)](https://travis-ci.org/cvhciKIT/sloth)

sloth is a tool for labeling image and video data for computer vision research.

The documentation can be found at http://sloth.readthedocs.org/ .

Latest Releases
===============

2013/11/29 v1.0: 2e69fdae40f89050fbaeef22491eee2a92e78b4f [.zip](https://github.com/cvhciKIT/sloth/archive/v1.0.zip) [.tar.gz](https://github.com/cvhciKIT/sloth/archive/v1.0.tar.gz)

For a full list, visit https://github.com/cvhciKIT/sloth/releases

修订版
=====
#### v1.0
为标注对象框加入 **颜色**设置功能(在配置文件中可以修改,如myconfig.py), 并修复了程序运行时的一些错误

#### v1.1
标注对象attributes属性扩展功能, 可以输入**固定值键值对**,**list数组**, **python type 对象**<br/>
其中在为键值对的值为**python type**类型时, 会在属性窗口中 出现一个 QLineEdit输入框, 修复了中文编码显示乱码以及在Json序列化时Unicode编码显示的一系列相关问题

#### v1.2
扩展色彩设置,加入画刷功能,也需要在 配置文件中修改,但是颜色设置要求更高,必须和画刷样式一起设置,或都不设置<br/>
2017/9/5
