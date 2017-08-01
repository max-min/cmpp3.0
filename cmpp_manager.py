



class cmppManager(object):


	def __init__(self):
		pass 

	#cmpp服务的入口函数
	@staticmethod
	def startCMPPService(message, telenumber):

		cmppManager.__initConfig()

		cmppManager.__connectISM()

		cmppManager.__submitMessage(message, telenumber)
		pass

	'''
 	@cmpp需要的配置信息
	'''
	@staticmethod
	def __initConfig():
		print("init")


	'''
 	@发起登录认证协议
	'''
	@staticmethod
	def __connectISM():
		print("connect")


	'''
	 @发送短信
	'''
	@staticmethod
	def __submitMessage(message, number):
		print("submit")

	#网关IP
	@staticmethod
	def getServerIP():
		return serverip
	

	#网关端口
	@staticmethod
	def getServerPort():
		return serverport
	
	#服务代码
	@staticmethod
	def getSrcID():
		return srcID

	#企业代码
	@staticmethod
	def getSPID():
		return SPID 

	
	# 业务代码
	@staticmethod
	def getServiceID():
		return serviceID

	#密码
	@staticmethod
	def getPassword():
		return pwd



if __name__ == "__main__":
	
	cmppManager.startCMPPService("Helloworld", "10086")




