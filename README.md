# myStockPro
股票小工具

# 环境说明
MAC电脑
现有版本：Python 2.7.16

# 准备
## brew install pyenv
### 安装
版本 pyenv 1.2.9
安装时间 5分钟+
$ pyenv init
提示"Load pyenv automatically by appending the following to ~/.zshrc"
（通过将以下内容附加到~/.zshrc，自动加载pyenv）
重启命令工具或者source ~/.zshrc
(注意：这个提示会一直存在，不用管，不影响后续)
### 常用命令
pyenv install --list  列出所有可以安装的版本
pyenv versions        当前可以使用的版本
pyenv install 3.6.0   安装指定的版本(时间有点长)
### 使用
pyenv local 3.6.0   目录下生效，会生成一个配置文件.python-version 文件
pyenv global 3.6.0  全局生效
pyenv shell 3.6.0   当前shell中生效

## pipenv
版本 version 2018.11.26
### 安装
brew install pipenv
### 初始化
初始用python3环境 pipenv --three
初始用python2环境 pipenv --two
初始用python具体版本环境 pipenv --python 3.6.0
在文件夹下有个 .venv的目录 ，这个就是该项目的虚拟环境
### 安装依赖
$ pipenv install flask
$ pipenv install pytest --dev 
### 查看依赖
pipenv graph





