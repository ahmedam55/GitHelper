from subprocess import Popen
import sublime, sublime_plugin,os
import subprocess

class logCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& gitk '+self.window.active_view().file_name()
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class ddCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git -no-color difftool -d'
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class dfCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git -no-color difftool '+self.window.active_view().file_name()+' -y'
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')

 
class bfCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git -no-color blame '+self.window.active_view().file_name()+'>h&&subl -w h && rm h'
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class cfCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git -no-color checkout '+self.window.active_view().file_name()
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class acCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git -no-color update-index --assume-unchanged '+self.window.active_view().file_name()
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class auCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git -no-color update-index --no-assume-unchanged '+self.window.active_view().file_name()
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class shCommand(sublime_plugin.WindowCommand):
    def run(self):
        beginline=str(self.window.active_view().rowcol(self.window.active_view().sel()[0].begin())[0]+1)
        endline=str(self.window.active_view().rowcol(self.window.active_view().sel()[0].end())[0]+1)

        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&&  git -no-color log --pretty=short -u -L '+beginline+','+endline+':'+self.window.active_view().file_name()+'>h && subl -w h && rm h'
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')


class oeCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd "' +self.window.project_data()['folders'][0]['path'] +'" &&  open .'
        sublime.set_clipboard(cmd_line)
        self.window.run_command('open_terminal')

        
