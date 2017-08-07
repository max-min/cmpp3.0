


'''
 cmpp 相关定义
'''

CMPP_CONNECT        = 0x00000001    #请求连接
CMPP_CONNECT_RESP   = 0x80000001    #请求连接应答
CMPP_TERMINATE      = 0x00000002	#终止连接
CMPP_TERMINATE_RESP = 0x80000002	#终止连接应答
CMPP_SUBMIT		  	= 0x00000004	#提交短信
CMPP_SUBMIT_RESP	= 0x80000004	#提交短信应答
CMPP_DELIVER		= 0x00000005	#短信下发
CMPP_DELIVER_RESP	= 0x80000005	#下发短信应答
CMPP_QUERY			= 0x00000006	#发送短信状态查询
CMPP_QUERY_RESP		= 0x80000006	#发送短信状态查询应答
CMPP_CANCEL			= 0x00000007	#删除短信
CMPP_CANCEL_RESP	= 0x80000007	#删除短信应答


class cmppUtil():

	
	static_sequenceId = 0;

	# 获取序列号
	@staticmethod
	def getSequenceId(self):
		return cmppUtil.static_sequenceId++


	# 生成时间戳明文格式 MMDDHHMMSS 
	@staticmethod
	def getTimestamp(self):
		pass 

	# 生成MD5 source_addr + 9字节0 + secret + timestamp
	@staticmethod
	def getAuthenticatorSource(self, sp_id, secret):
		pass

	#写入指定长度的字符串，不足补0
	@staticmethod
	def writeString(self, fd, msgbuffer, msglen):
		pass


