
'''
	@ 发送短信后回应处理

'''
class cmppSubmitResp(cmppHeadder):
	
	def __init(self, respMessage):
		if len(respMessage) == (12 + 8+ 4):
			self.setTotalLength(struct.unpack('!I', RespMessage[0:4]))
			self.setCommanId(struct.unpack('!I', RespMessage[4:8]))
			self.setSequence_id(struct.unpack('!I', RespMessage[8:12]))

			#body 
			self.msgId = struct.unpack('!L', RespMessage[12:20])
			self.result = struct.unpack('!I', RespMessage[20:24])
		else:
			print('respMesage len error:' + len(respMessage))

	def getMsgId(self):
		return self.msgId


	def getResult(self):
		return self.result