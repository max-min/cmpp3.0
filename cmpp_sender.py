

'''
	cmppSender:发送处理对象，以及接受消息
'''

class cmppSender(object):

	def __init__(self, socketfd, message):
		self.sockFd = socketfd
		self.message = message


	def sendMsg():
		if self.sockFd != 0 and self.message != "":
			cmppNet.sendMsg(sockFd, message)
			
