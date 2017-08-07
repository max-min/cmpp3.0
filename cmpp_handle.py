

'''
 cmpp 认证和短信的主要处理接口实现
'''
class cmppHandle(object):


	@staticmethod
	def connectISMG(ip, port):
		sockFd = cmppNet.startTcpClient(0, ip, port, None)
		if  sockFd > 0 :
			connObj = cmppConnect()
			connObj.setTotalLength(12+6+16+1+4)
			connObj.setCommandId(CMPP_CONNECT)
			connObj.setSequenceId(cmppUtil.getSequenceId())
			connObj.setSourceAddr(cmppManager.getSPID())
			connObj.setAuthenticatorSource(cmppUtil.getAuthenticatorSource(cmppManager.getSPID(), cmppManager.getPassword()))
			
			connObj.setVersion(0x0F)
			connObj.setTimestamp(MMDDHHMMSS)
		else:
			print("conenct error:" + ip + ", " + port)
			rzturn -1

		sendObje = cmppSender(sockFd, message)
		