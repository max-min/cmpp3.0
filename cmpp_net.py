

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
		pass

	'''
		@remarks: 穿件socket客户端连接
		@flags  : tcp/udp
		@ip/port: 需要连接的ip和端口信息
		@callbackFunc 收到消息的回调接口
	'''
	@staticmethod
	def startTcpClient(flags, ip , port, callbackFunc):
		sockFd = 0;
		if flags == 0:
			sockFd = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		else:
			sockFd = ssocket.socket(socket.AF_INET, socket.SOCKET_DGRAM)

		try:
			sockFd.connect((ip, port))
		except socket.error, msg:
    		print 'Failed to  connect [' +ip ', '+ port +'], Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
		
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

	