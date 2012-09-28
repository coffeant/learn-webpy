# coding=utf-8
from controller.base.FrameController import FrameController
import web
import model.user.UserLogin

class LoginResult(FrameController):
	def process(self):
		i = web.input()
		
		m = model.user.UserLogin.UserLogin()
		r = m.select({'loginname':i.loginname,'password':m.str_md5(i.password)})
		
		if len(r) > 0:
			self.setVariable('msg','登录成功')
		else:
			self.setVariable('msg','登录失败')
