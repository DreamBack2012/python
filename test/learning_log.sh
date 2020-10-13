#!/bin/bash

# 搭建learning_log的脚本，注意，只能在Linux环境下执行

# 启动虚拟环境
function virtualenv_start(){
    # 新建项目目录，创建与文件名一样的目录
    project=${0%.*}
    if [ ! -d $project ];then
        mkdir -p $project
    fi

    # 切换至工程目录
    cd $project

    # 确认安装了虚拟环境
    python3_venv=`dpkg -l | grep python3-venv | awk '{print $2}'`
    if [ "$python3_venv" != "python3_venv" ];then
        sudo apt-get install python3-venv
    fi

    # 创建虚拟环境
    python3 -m venv ll_env

    # 激活虚拟环境（停止使用寻环境，使用命令deactive，或者关闭运行虚拟环境的终端即可）
    source ll_env/bin/activate

}

env_build
