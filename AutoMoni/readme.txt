#程序支持搭建的linux服务器上，window未测试。(请联网安装应用环境)
#程序需要python2.7及以上python版本支持，需要使用python库：psutil,paramiko
#1 如何使用本程序：
1.搭建基础环境：
    # 将安装包放到你的代理服务器网站目录下，将安装包同时放到你的服务器机器和代理服务器相同目录下（必须相同目录）
    # 安装pip和必要的依赖库      
    # 执行pip install -r requirements.txt，进入python shell中确认psutil，paramiko库安装正确
    # 在客户端机器上修改conffile.py文件配置你的代理服务器信息。
    # 在代理服务器和客户端服务器process.txt文件中配置你要监控的程序进程。
    # 在客户端机器上执行agent.sh脚本。
    # 在代理服务器上运行server.sh脚本。
    # 在网页上打开你的自动化监控页面即可使用

#2 本程序已知bug：
1.当监控的进程不存在时，启动收集数据程序会生成 process: unrecognized service。
2.在判断进程是否running时，如果状态为stopping则为红色背景，但当状态为running是背景也为红色。
3.前端页面很丑，哈哈。。。
