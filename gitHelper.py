from subprocess import Popen
import sublime, sublime_plugin,os
import subprocess

class logCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& gitk '+self.window.active_view().file_name()
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # out = p.communicate()[0]
        # print(out)
        # p=subprocess.Popen("sudo sh ~/gitk.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # out = p.communicate()[0]
        # print(out)


class ddCommand(sublime_plugin.WindowCommand):
    def run(self):
        # cmd_line = 'cd "' +self.window.project_data()['folders'][0]['path'] +'" && sh gittt.sh'
        # installed_dir,_=__name__.split('.')
        # package_dir = os.path.join(sublime.packages_path(), installed_dir)
        # p = subprocess.Popen([r'/Users/ahmed/Library/Application Support/Sublime Text 3/Packages/gitHelper/terminal.sh'], cwd=r"/Users/ahmed/Library/Application Support/Sublime Text 3/Packages/gitHelper/")
        # os.system('''tell application "Terminal" do shell script "open -a firefox" ''')
        # os.system(''' sh "/Users/ahmed/Library/Application Support/Sublime Text 3/Packages/gitHelper/terminal.sh" ''')
        # subprocess.Popen(["/Users/ahmed/Library/Application Support/Sublime Text 3/Packages/gitHelper/terminal.sh"] ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # print(p.communicate())
        # print(installed_dir,package_dir)
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git difftool -d'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

class dfCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git difftool '+self.window.active_view().file_name()+' -y'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # os.system('''osascript -e 'tell application "python" to activate' ''')
 
class bfCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git blame '+self.window.active_view().file_name()+'>h&&subl -w h && rm h'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

class cfCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git checkout '+self.window.active_view().file_name()
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

class acCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git update-index --assume-unchanged '+self.window.active_view().file_name()
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

class auCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&& git update-index --no-assume-unchanged '+self.window.active_view().file_name()
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

class shCommand(sublime_plugin.WindowCommand):#fdsfsdf
    def run(self):
        beginline=str(self.window.active_view().rowcol(self.window.active_view().sel()[0].begin())[0]+1)
        endline=str(self.window.active_view().rowcol(self.window.active_view().sel()[0].end())[0]+1)

        cmd_line = 'cd ' +self.window.project_data()['folders'][0]['path'] +'&&  git log --pretty=short -u -L '+beginline+','+endline+':'+self.window.active_view().file_name()+'>h && subl -w h && rm h'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


# unrelated
class oeCommand(sublime_plugin.WindowCommand):
    def run(self):
        cmd_line = 'cd "' +self.window.project_data()['folders'][0]['path'] +'" &&  open .'
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
