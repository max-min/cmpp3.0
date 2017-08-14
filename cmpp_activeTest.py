

'''
	@向ISMG发送保活心跳

'''
from cmpp_header import * 
class cmppActiveTest(cmppHeader):
	def __init__(self):
		pass 


		#字节流的形式写入buffer
	def writeToByteBuffer(self):
		return struck.pack('!III', self.getTotalLength(), self.getCommandId(), self.getSequenceId())





