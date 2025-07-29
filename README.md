# Telegram-name-update-stable-fix-version
Telegram name update stable fix version
参考文档：<a href="https://telethon.readthedocs.io/en/stable/">Telethon</a>
lastname实时更新效果：<a href="https://t.me/LiTuZi">Cody</a>

## 0. 准备
运行环境：VPS，python3，python3-pip

创建应用：<a href="https://my.telegram.org/">https://my.telegram.org/</a>。只要填App title和Short name即可。获得api_id和api_hash。

安装 Python 3（Python3安装教程只行搜索）

## 1. 安装步骤与项目地址
<code>git clone [https://github.com/lituzi888/Telegram-name-update-stable-fix-version](https://github.com/lituzi888/Telegram-name-update-stable-fix-version) </code>

安装完Python3后下载项目到本机，打开项目压缩包里的tg_username_update.py修改里面的api_id与api_hash保存

上传项目到云服务器root目录里并解压

在项目目录里命令执行安装telethon

pip3 install -r requirements.txt

运行项目 

python3 tg_username_update.py

根据提示输入你的tg手机号与验证码（如有二级验证码也需要输入）

挂后台 

nohup python3 tg_username_update.py &


如遇见emojize 报错 换版本

pip3 install emoji==1.6.3

