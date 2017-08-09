

'''
	cmppSender:发送处理对象，以及接受消息
'''

class cmppSender(object):

	def __init__(self, socketfd, message):
		self.sockFd = socketfd
		self.message = message


	def senderSevice():
		if self.sockFd != 0 and self.message != "":
			cmppNet.sendMsg(sockFd, message)
		else:
			print('socket or message error, sockfd=' + sockFd + 'messsage:' + message)
			return -1

		if cmppNet.recvMsg(sockFd, RecvMessage, msgLen)  > 0:
			if msgLen > 8:
				recvHeader = cmppHeader(RecvMessage)
				if( recvHeader.getCommandId() == CMPP_CONNECT_RESP):
					connectResp = cmppConnectResp()

				elif(recvHeader.getCommandId() == CMPP_SUBMIT_RESP):
					submitResp = cmppSubmitResp()
					pass
				elif(recvHeader.getCommandId() == CMPP_ACTIVE_TEST):
					activeResp = cmppActiveTestResp()
					pass
				elif(recvHeader.getCommandId() == CMPP_ACTIVE_TEST_RESP):
					print('the active test resp')
				else:
					print('unknow the msg command:' + recvHeader.getCommandId())
		else:
			print('recv the message error' + RecvMessage)
			return -1
		

			
