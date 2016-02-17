from subprocess import call
import sublime, sublime_plugin

class logCommand(sublime_plugin.WindowCommand):
    def run(self):
    	os.system('cd ' +self.window.project_data()['folders'][0]['path'] +'&& gitk '+self.window.active_view().file_name()+'&& pause')

    	# print(self.window.active_view().file_name())
