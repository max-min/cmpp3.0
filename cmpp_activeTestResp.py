
'''
	@保活心跳回应处理

'''

from cmpp_header import * 

class cmppActiveTestResp(cmppHeader):
	

	def __init__(self, RespMessage):
		if len(RespMessage) == 12:
			self.setTotalLength(struct.unpack('!I', RespMessage[0:4]))
			self.setCommanId(struct.unpack('!I', RespMessage[4:8]))
			self.setSequence_id(struct.unpack('!I', RespMessage[8:12]))

	def getReserved(self):
		return self.Reserved

	def setReserved(self, Reserved):
		self.Reserved = Reserved

     		#字节流的形式写入buffer
	def writeToByteBuffer(self):
		return struck.pack('!IIIC', self.getTotalLength(), self.getCommandId(), self.getSequenceId(), self.getReserved())

