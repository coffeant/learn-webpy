# -*- coding: utf-8 -*-

class View(object):
	def __init__(self):
		self.m_templatePath = ''
		self.m_variableDict = dict()
		self.m_dictSubView = dict()
		self.m_parentView = None
		
		# a cache variable
		self.m_rootView = None
		
	def render(self,render):
		varDict = dict(self.variableDict())
		
		for name in self.m_dictSubView:
			aSubView = self.m_dictSubView[name]
			varDict[name] = aSubView.render(render)
		
		r = render.frender(self.m_templatePath)
		return r( varDict )
		
	def setTemplatePath(self,strTemplatePath):
		self.m_templatePath = strTemplatePath
		
	def setVariable(self,key,value):
		self.m_variableDict[key] = value
		
	def variableDict(self):
		return self.m_variableDict
		
	def addSubView(self,strName,aView):
		self.m_dictSubView[strName] = aView
		aView.setParentView(self)
		
	def subView(self,strName):
		return self.m_dictSubView[strName]
		
	def subViewIterator(self):
		pass
		
	def setParentView(self,aView):
		self.m_parentView = aView
		
		# clean cache variable when parent view change
		self.m_rootView = None
		
	def parentView(self):
		return self.m_parentView
		
	def rootView(self):
		if self.m_rootView :
			return self.m_rootView
		else:
			if self.m_parentView:
				self.m_rootView = self.m_parentView.rootView()
				return self.m_rootView
			else:
				return self