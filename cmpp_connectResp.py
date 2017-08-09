
'''
	@ 认证成功后解析处理回应状态
'''

class cmppConnectResp(cmppHeader):
	def __init(self, RespMessage):

		# header 
		self.setTotalLength(struct.unpack('!I', RespMessage[0:4]))
		self.setCommanId(struct.unpack('!I', RespMessage[4:8]))
		self.setSequence_id(struct.unpack('!I', RespMessage[8:12]))

		#body 
		self.status = struct.unpack('!I', RespMessage[12:16])
        self.authenticator_ISMG = RespMessage[16:32]
        self.version = struct.unpack('!B', message_body[32:33])
