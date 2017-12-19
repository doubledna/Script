#程序支持搭建的linux服务器上，window未测试。(请联网安装应用环境)
#程序需要python2.7及以上python版本支持，需要使用python库：psutil,paramiko
#1 如何使用本程序：
1.搭建基础环境：
    # 安装依赖包：
	             
	# 执行pip install -r requirements.txt
	# 

#2 本程序存在的问题：
1.当监控的进程不存在时，启动收集数据程序会生成 process: unrecognized service。
2.在判断进程是否running时，如果状态为stopping则为红色背景，但当状态为running是背景也为红色。