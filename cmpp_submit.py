

'''
	@向短信网关发送消息

'''

class cmppSubmit(cmppHeader):

	def __init__(self):
		super.__init__()


	MsgId = 0;  #信息标示
	Pk_total = 0x01; #相同的msgId总数，从1开始
	Pk_number = 0x01 #想用的msgId序号，从1开始
	Registered_Del = 0x00; #是否要求返回状态报告，0不需要，1需要
	Msg_level = 0x01 #信息级别
	Service_Id = "" #业务标示，企业代码
	Fee_UserType = 0x00 #用户计费类型， 谁接收，计谁的费
	Fee_terminal_Id = ""  #被计费的号码
	Fee_terminal_Type = 0x00 #被计费号码的类型，真实号码或者虚拟号码
	TP_pId = 0x00
	TP_udhi = 0x00
	Msg_Fmt = 0x0f #信息格式 15含GB汉字
	Msg_src    #企业代码
	
	'''
		01：对“计费用户号码”免费；
		02：对“计费用户号码”按条计信息费；
	 	03：对“计费用户号码”按包月收取信息费
	'''
	FeeType = "01" #资费类型， 默认为按条计费
	FeeCode = "5" 
	ValId_Time = "" #暂不支持
	At_Time = "" #暂不支持
	
	#SP的服务代码或前缀为服务代码的长号码,
	#网关将该号码完整的填到SMPP协议Submit_SM消息相应的source_addr字段，该号码最终在用户手机上显示为短消息的主叫号码。
	Src_Id
	DestUsr_tl = 0x01 #不支持群发
	Dest_Terminal_Id  #接收手机号码，
	Dest_Terminal_type = 0x00  #真实号码
	Msg_Length
	Msg_Content #信息内容
	#点播业务使用的LinkID，非点播类业务的MT流程不使用该字段
	LinkID = ""



	def getMsgId(self):
		return self.MsgId
	def setMsgId(self, id):
		self.MsgId = id 

	def getPk_total(self):
		return self.Pk_total
	def setPk_total(self,total):
		self.Pk_total = tatal

	def getPk_number(self):
		return self.Pk_number
	def setPk_number(self,number):
		self.Pk_number = number	

	def getRegistered_Del(self):
		return self.Registered_Del
	def setRegistered_Del(self,Registered_Del):
		self.Registered_Del = Registered_Del

	def getMsg_level(self):
		return self.Msg_level
	def setMsg_level(self,Msg_level):
		self.Msg_level = Msg_level

	def getService_Id(self):
		return self.Service_Id
	def setService_Id(self,Service_Id):
		self.Service_Id = Service_Id

	def getFee_UserType(self):
		return self.Fee_UserType
	def setFee_UserType(self,Fee_UserType):
		self.Fee_UserType = Fee_UserType

	def getFee_terminal_Id(self):
		return self.Fee_terminal_Id
	def setFee_terminal_Id(self,Fee_terminal_Id):
		self.Fee_terminal_Id = Fee_terminal_Id

	def getFee_terminal_Type(self):
		return self.Fee_terminal_Type
	def setFee_terminal_Type(self,Fee_terminal_Type):
		self.Fee_terminal_Type = Fee_terminal_Type

	def getTP_pId(self):
		return self.TP_pId
	def setTP_pId(self,TP_pId):
		self.TP_pId = TP_pId

	def getTP_udhi(self):
		return self.TP_udhi
	def setTP_udhi(self,TP_udhi):
		self.TP_udhi = TP_udhi

	def getMsg_Fmt(self):
		return self.Msg_Fmt
	def setMsg_Fmt(self,Msg_Fmt):
		self.Msg_Fmt = Msg_Fmt

	def getMsg_src(self):
		return self.Msg_src
	def setMsg_src(self,Msg_src):
		self.Msg_src = Msg_src

	def getFeeType(self):
		return self.FeeType
	def setFeeType(self,FeeType):
		self.FeeType = FeeType

	def getFeeCode(self):
		return self.FeeCode
	def setFeeCode(self,FeeCode):
		self.FeeCode = FeeCode

	def getValId_Time(self):
		return self.ValId_Time
	def setValId_Time(self,ValId_Time):
		self.ValId_Time = ValId_Time

	def getAt_Time(self):
		return self.At_Time
	def setAt_Time(self,At_Time):
		self.At_Time = At_Time

	def getSrc_Id(self):
		return self.Src_Id
	def setSrc_Id(self,Src_Id):
		self.Src_Id = Src_Id

	def getDestUsr_tl(self):
		return self.DestUsr_tl
	def setDestUsr_tl(self,DestUsr_tl):
		self.DestUsr_tl = DestUsr_tl

	def getDest_Terminal_Id(self):
		return self.Dest_Terminal_Id
	def setDest_Terminal_Id(self,Dest_Terminal_Id):
		self.Dest_Terminal_Id = Dest_Terminal_Id

	def getDest_Terminal_type(self):
		return self.Dest_Terminal_type
	def setDest_Terminal_type(self,Dest_Terminal_type):
		self.Dest_Terminal_type = Dest_Terminal_type

	def getMsg_Length(self):
		return self.Msg_Length
	def setMsg_Length(self,Msg_Length):
		self.Msg_Length = Msg_Length

	def getMsg_Content(self):
		return self.Msg_Content
	def setMsg_Content(self,Msg_Content):
		self.Msg_Content = Msg_Content

	def getLinkID(self):
		return self.LinkID
	def setLinkID(self,LinkID):
		self.LinkID = LinkID


	#字节流的形式写入buffer
	def writeToByteBuffer(self):
		length = self.getMsg_Length()
		return struct.pack('!III LBBB BB10sB 32sBBB B6sH6s 17s17s21sB 32sBB{length}s20s'.format(length),
			self.getTotalLength(), self.getCommandId(), self.getSequenceId(),
			self.getMsgId(), self.getPk_total(), self.getPk_number(), self.getRegistered_Del(),
			self.getMsg_level(), self.getService_Id(), self.getFee_UserType(), self.getFee_terminal_Id(),
			self.getFee_terminal_Type(), self.getTP_pId(), self.getTP_udhi(), self.getMsg_Fmt(),
			self.getMsg_src(), self.getFeeType(), self.getFeeCode(), self.getValId_Time(),
			self.getAt_Time(), self.getSrc_Id(), self.getDestUsr_tl(), self.getDest_Terminal_Id(), 
			self.getDest_Terminal_type(), self.getMsg_Length(), self.getMsg_Content(), self.getLinkID())