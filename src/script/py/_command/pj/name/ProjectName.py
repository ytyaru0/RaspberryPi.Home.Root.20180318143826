import sys, os.path, pathlib
sys.path.append(str(pathlib.Path(__file__).parent))
sys.path.append(os.path.expanduser('~/root/_meta/path/'))
from PathIni import PathIni
from Command import Command
from ExtToLang import ExtToLang
import datetime

class ProjectName:
    def __init__(self):
        self.__path_target = None
        #self.__path_target = os.path.join(PathIni()['root_db_meta_programming'], "languages.yml")

    def Generate(self, commands:list)->str:
        lang = ExtToLang().To(commands[0])
        dt = '{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
        categolies, tpl_var_dict = Command().Analize(commands)
        #print(lang, dt, tpl_var_dict )
        if 'dirname' in tpl_var_dict: return tpl_var_dict['dirname']
        elif '_0' in tpl_var_dict: return lang + '.' + tpl_var_dict['_0'] + '.' + dt 
        else: return lang + '.' + dt


if __name__ == '__main__':
    print(ProjectName().Generate('pj py test -MyDirName'.split(' ')))
