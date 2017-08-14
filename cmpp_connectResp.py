
'''
	@ 认证成功后解析处理回应状态
'''
from cmpp_header import * 
dictStatus = {0:'正确', 1:'消息结构错误', 2:'非法源地址', 3:'认证错', 4:'版本太高', 5:'其他错误'}

class cmppConnectResp(cmppHeader):

    def __init__(self, RespMessage):
        sureLen=12+4+16+1
        if len(RespMessage) == sureLen:
            self.setTotalLength(struct.unpack('!I', RespMessage[0:4]))
            self.setCommanId(struct.unpack('!I', RespMessage[4:8]))
            self.setSequence_id(struct.unpack('!I', RespMessage[8:12]))
            #body 
            tmpstatus = struct.unpack('!I', RespMessage[12:16])
            self.setStatus(tmpstatus)
            self.authenticator_ISMG = RespMessage[16:32]
            self.version = struct.unpack('!B', RespMessage[32:33])
        else:
            print('respMessage len error:' + len(RespMessage))


    def getStatus(self):
    	return self.status

    def setStatus(self, status):
    	if dictStatus.get(status, '') != '':
    		return dictStatus[status]
    	else:
    		return '未知错误'


    def getAuthenticator_ISMG(self):
    	return self.authenticator_ISMG

    def getVersion(self):
    	return self.version