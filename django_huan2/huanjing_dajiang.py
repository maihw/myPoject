#首先在终端命令行更新 pip3
sudo pip3 install -U pip

#安装 Django2 的最终版本 2.2.9
pip install django==2.2.9

#此外我们还要安装一些其它的基础工具包，先安装 ipython 
#和 mysqlclient 这两个，其它的在需要时再进行安装
pip install ipython mysqlclient

#使用命令 pip freeze 查看当前 python 环境下已经安装的各种包及其依赖包
pip freeze