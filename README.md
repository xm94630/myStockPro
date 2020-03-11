# myStockPro
股票小工具

# 环境说明
MAC电脑
现有版本：Python 2.7.16

# python 准备
## pyenv
### 安装
brew install pyenv 安装时间 5分钟+
### 初始化
$ pyenv init
提示"Load pyenv automatically by appending the following to ~/.zshrc"（通过将以下内容附加到~/.zshrc，自动加载pyenv）
### 添加配置
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
重启命令工具或者source ~/.zshrc
(注意：这个提示会一直存在，不用管，不影响后续)
### 常用命令
pyenv install --list  列出所有可以安装的版本
pyenv versions        当前可以使用的版本
pyenv install 3.7.2   安装指定的版本(时间有点长)
### 使用
pyenv local 3.7.2   目录下生效，会生成一个配置文件.python-version 文件
pyenv global 3.7.2  全局生效
pyenv shell 3.7.2   当前shell中生效

## pyenv-virtualenv
brew install pyenv-virtualenv

## pipenv
版本 version 2018.11.26
### 安装
brew install pipenv
### 初始化
初始用python具体版本环境 pipenv --python 3.7.2
在文件夹下有个 .venv的目录 ，这个就是该项目的虚拟环境
### 安装依赖
$ pipenv install flask
$ pipenv install pytest --dev 
### 查看依赖
pipenv graph
### 线上版本，下载很慢的
https://www.python.org/downloads/source/
我已经下载了一个 Python-3.7.2.tar.xz 存在项目中，以备不时之需

# 最终开发版本
python 3.7.2 (使用pyenv切换到此环境)
pip 18.1
pyenv 1.2.9 (pipenv --python 3.7.2 这个有点慢，时间在5-10分钟 会生成一个Pipfile)
pipenv version 2018.11.26





