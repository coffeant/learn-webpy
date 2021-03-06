# -*- coding: utf-8 -*-

import WebPageController
import view.View
import web
import model.Model
import system.session

class FrameController(WebPageController.WebPageController):
	def __init__(self):
		super(FrameController,self).__init__()
		
		self.setVariable('path',self.m_path)
		
		self.addPostProcess('user')
		
	def buildView(self):
		aBodyView = view.View.View()
		aBodyView.setTemplatePath(self.m_path.replace('.','/'))
		self.setView(aBodyView)
		
		aPageView = view.View.View()
		aPageView.setTemplatePath('frame/frontpage')
		aPageView.addSubView('body',aBodyView)
		
		aFrameView = view.View.View()
		aFrameView.setTemplatePath('frame/frame')
		aFrameView.addSubView('body',aPageView)
		
	def ppUser(self):
		# session
		s = system.session.Session.singleton()
		uid = -1
		if hasattr(s,'uid'):
			uid = s['uid']
		self.setVariable('uid',uid)
		
		# userinfo
		if hasattr(s,'userinfo'):
			self.setVariable('frame_userinfo',s['userinfo'])
