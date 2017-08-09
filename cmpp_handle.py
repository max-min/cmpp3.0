

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
			
			connObj.setVersion(CMPP_VERSION)
			connObj.setTimestamp(time.strftime('%m%d%H%M%S', time.localtime(time.time())))
		else:
			print("conenct error:" + ip + ", " + port)
			return -1

		message = connObj.writeToByteBuffer()
		sendObjc = cmppSender(sockFd, message)
		return sendObjc.sendService()
