

'''
	@所有请求的消息头
	@totalLength 消息长度
	@commandid 消息ID
	@sequence  流水号，顺序累加，一对请求回应，流水号相同

'''

class cmppHeader(object):
	def __init__(self, recvMessage):
		self.setTotalLength(struct.upack('!I', recvMessage[0:4]))
		self.setCommanId(struct.upack('!I', recvMessage[4:8]))
		self.setSequence_id(struct.upack('!I', recvMessage[8:12]))

	#
	def getTotalLength(self):
		return self.total_length

	def setTotalLength(self, total_length):
		self.total_length = total_length

	def getCommandId(self):
		return self.command_id

	def setCommanId(self, command_id):
		self.command_id = command_id

	
	def setSequence_id(self, sequence_id):
		self.sequence_id = sequence_id

	def toStringBuffer(self, msg):
		pass 


	# 字节流的形式写入buffer
	def writeToByteBufferr(self):
		return struct.pack("!III", self.total_length, self.command_id, self.sequence_id)

	
	# 读取字节流中的int类型
	def readToByteBufferr(self, resp_msg):
		self.total_length,self.command_id,self.sequence_id=struct.upack('!III', resp_msg)





	