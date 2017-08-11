

'''
 cmpp 认证和短信的主要处理接口实现
'''
class cmppHandle(object):


	#认证
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

		conncMessage = connObj.writeToByteBuffer()
		sendObjc = cmppSender(sockFd, conncMessage)
		return sendObjc.sendService()

	# 发送短信
	@staticmethod
	def sendMessage(sockFd, message, number):
		if sockFd <= 0 or message == '' or number == '':
			print('param error')
			return -1

		submitObj = cmppSubmit()
		#header
		submitObj.setTotalLength(12+8+1+1+1+1+10+1+32+1+1+1+1+6+2+6+17+17+21+1+32+1+1+msg.length()*2+20)
		submitObj.setCommandId(CMPP_SUBMIT)
		submitObj.setSequenceId(cmppUtil.getSequenceId())
		#body
		submitObj.setMsgId(0x00)
		submitObj.setPk_total(0x01)
		submitObj.setPk_number((byte)0x01)			
		submitObj.setRegistered_Del(0x00)
		submitObj.setMsg_level(0x01)

		submitObj.setService_Id(cmppManager.getServiceID())
		submitObj.setFee_UserType(0x02)
		submitObj.setFee_terminal_Id('')
		submitObj.setFee_terminal_Type(0x00)
		submitObj.setTP_pId(0x00);
		submitObj.setTP_udhi(0x00);
		submitObj.setMsg_Fmt(0x0F);
		submitObj.setMsg_src(cmppManager.getSPID()) 
		
		submitObj.setFeeType('01')
		submitObj.setFeeCode('5')
		submitObj.setValId_Time('')
		submitObj.setAt_Time('')
		submitObj.setSrc_Id(CMPPManager.getSrcID())
		submitObj.setDestUsr_tl(0x01)

		submitObj.setDest_Terminal_Id(number)
		submitObj.setDest_Terminal_type(0x00)

		submitObj.setMsgLength(len(message))
		submitObj.setMsg_Content(message)
		submitObj.setLinkID('')

		submitMessage = submitObj.writeToByteBuffer()
		sendObjc = cmppSender(sockFd, submitMessage)
		return sendObjc.sendService()

	#心跳保活连接
	@staticmethod
	def sendActiveTest(sockFd):
		activeTestObj = cmppActiveTest()
		active.setTotalLength(12) #消息总长度，级总字节数:4+4+4(消息头)
		active.setCommandId(CMPP_ACTIVE_TEST) 
		active.setSequenceId(cmppUtil.getSequenceId()) #序列，由我们指定

		activeTestMessage = activeTestObj.writeToByteBuffer()

		sendObj = cmppSender(sockFd, activeTestMessage)
		return sendObj.sendService()

	#心跳回应处理
	staticmethod
	def sendAciveTestResp(sockFd, recvmessage):
		activeRespObj = cmppActiveTestResp(recvmessage)
		activeRespObj.setTotalLength(12+1)
		activeRespObj.setCommandId(CMPP_ACTIVE_TEST_RESP)
		#activeRespObj.setSequenceId()构造函数中提取之前activetest中的sequenceid
		activeRespObj.setReserved(0x00)

		activeRespMessage = activeRespObj.writeToByteBuffer()

		sendObjc = cmppSender(sockFd, activeRespMessage)
		return sendObjc.sendService()
		


