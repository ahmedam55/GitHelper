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

class shCommand(sublime_plugin.WindowCommand):
	def run(self):
		beginline=str(self.window.active_view().rowcol(self.window.active_view().sel()[0].begin())[0]+1)
		endline=str(self.window.active_view().rowcol(self.window.active_view().sel()[0].end())[0]+1)

		p=Popen(['CMD ',' /c cd ' +self.window.project_data()['folders'][0]['path'] +'&& git log --pretty=short -u -L '+beginline+','+endline+':'+self.window.active_view().file_name()+'>h&&subl -w h && del h'])


# unrelated
class oeCommand(sublime_plugin.WindowCommand):
	def run(self):
		p=Popen(['CMD ',' /c explorer ' +self.window.project_data()['folders'][0]['path']])