
'''
	向短信网关发送认证请求
'''

class cmppConnect(cmppHeader):

	def __init__(self):
		pass 

	# 源地址 也就是企业代码 sp_id
	def getSourceAddr(self):
		return self.souce_addr 
	def setSourceAddr(self, sp_id):
		self.source_addr = sp_id 


	#用于鉴别源地址。其值通过单向MD5 hash计算得出，表示如下：
	#AuthenticatorSource = MD5（Source_Addr+9 字节的0 +shared secret+timestamp） Shared secret 
	#由中国移动与源地址实体事先商定，timestamp格式为：MMDDHHMMSS，即月日时分秒，10位。
	def getAuthenticatorSource(self):
		return self.authenticator_source
	def setAuthenticatorSource(self, source):
		self.authenticator_source = source 

	#双方协商的版本号(高位4bit表示主版本号,低位4bit表示次版本号)，对于3.0的版本，高4bit为3，低4位为0
	def getCMPPVersion(self):
		return self.version
	def setCMPPVersion(self, version):
		self.version = version


	#时间戳的明文,由客户端产生,格式为MMDDHHMMSS，即月日时分秒，10位数字的整型，右对齐 。
	def getTimestamp(self):
		return self.timestamp
	def setTimestamp(self, time):
		self.timestamp = time


	#字节流的形式写入buffer
	def writeToByteBuffer():
		return struck.pack('iii6s16sci', self.getTotalLength(), self.getCommandId(), self.getSequenceId(),
			self.getSourceAddr(), self.getAuthenticatorSource(), self.getCMPPVersion(), self.getTimestamp())

