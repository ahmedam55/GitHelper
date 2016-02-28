from subprocess import Popen
import sublime, sublime_plugin,os


class logCommand(sublime_plugin.WindowCommand):
    def run(self):
    	p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& gitk '+self.window.active_view().file_name()])


class ddCommand(sublime_plugin.WindowCommand):
    def run(self):
    	p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git difftool -d'])


class dfCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git difftool '+self.window.active_view().file_name()+' -y'])

class bfCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git blame '+self.window.active_view().file_name()+'>h&&subl -w h && del h'])

class cfCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git checkout '+self.window.active_view().file_name()])

class acCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git update-index --assume-unchanged '+self.window.active_view().file_name()])

class auCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git update-index --no-assume-unchanged '+self.window.active_view().file_name()])







# unrelated
class oeCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c explorer ' +self.window.project_data()['folders'][0]['path']])