# 北邮portal openwrt校园网自动认证脚本
注：本项目包含两个分支，v1.0版本固定认证地址，代码十分简单 v1.1可动态获取认证地址，但是为了尽量减少额外包的安装，代码有些抽象

## 使用指南
重要提示：本脚本在op有梯子环境下可能无法正常使用

op 默认是不带python环境的，因此在中继校园网之前我们需要安装python环境

怎么安装呢？

手机开热点！op联网之后执行下面命令安装python：

```
# python 和pip 安装
opkg install python3-base
opkg install python3-pip
opkg install python3
```

安装完成后可以命令行输python 测试一下



`pip install requests`  安装requests的库


安装完成后,把代码上传到op后台，把connect.py中的username 和 password 改成你的学号和上网密码

![image-20241120185656031](https://r2img.xianrenzhou.top/pics/2024/11/6867ca445f263f4c8bb0b22a120c7db9.png)

 `chmod +x connect.py`
 
 给运行脚本可执行权限



然后打开op管理界面，找到计划任务

![image-20241120185852789](https://r2img.xianrenzhou.top/pics/2024/11/74c20639b87f3d9867510485b5449534.png)

添加 `*/5 * * * * ~/connect.py > connect_log.txt`(~/connect.py换成connect.py的路径)

然后在启动项中重启cron即可


