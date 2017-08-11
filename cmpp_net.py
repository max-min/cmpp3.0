

'''
	创建相关网络socket，并进行一些消息的收发处理
	和CMPP协议无关。独立模块

'''

import socket 

class cmppNet(object):


	'''
		@remarks:创建socket服务端服务 
		@flags  tcp/udp
		@port   监听端口
		@callbackFunc 收到消息的回调接口
	'''
	@staticmethod
	def startTcpService(flags, port, callbackFunc):
		for i in range(len(cmppNet.listenList)):
			tup = cmppNet.listenList[i]
			if tup[0] == port:
				if tup[1] > 0:
					return tup[1] # 返回socketFd
				else:
					cmppNet.listenList.pop(i)

		sockFd = 0;
		if flags == 0:
			sockFd = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		else:
			sockFd = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)

		try:
			sockFd.bind(('127.0.0.1', port))
		except socket.error:
			print('Failed to connect')
			sockFd = -1
		sockFd.listen(10)
		# create a thread to accept 
		 '''
			while True 
				connct, addr  = sockFd.accept()
		 '''
		tup = (port, sockFd)
		cmppNet.listenList.append(tup)
		return sockFd

	'''
		@remarks: 穿件socket客户端连接
		@flags  : tcp/udp
		@ip/port: 需要连接的ip和端口信息
		@callbackFunc 收到消息的回调接口
	'''
	@staticmethod
	def startTcpClient(flags, ip, port, callbackFunc):
		#tmpaddress = (ip, port)
		for i in range(len(cmppNet.connectList)):
			tup = cmppNet.connectList[i]
			if tup[0] == ip and tup[1] == port:
				return tup[3]

		sockFd = 0;
		if flags == 0:
			sockFd = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		else:
			sockFd = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)

		try:
			sockFd.connect((ip, port))
		except socket.error:
			print('Failed to connect')
			sockFd = -1
		tup = (ip, port, sockFd)
		cmppNet.connectList.append(tup)
		return sockFd
		


	'''
		发送消息
	'''
	@staticmethod
	def sendMsg(sockFd, msg, len):
		pass 

	@staticmethod
	def recvMsg(sockFd, msg, len):
		pass 

	