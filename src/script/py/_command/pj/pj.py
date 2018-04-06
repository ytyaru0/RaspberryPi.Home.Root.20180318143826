import sys, os.path, pathlib
sys.path.append(os.path.expanduser('~/root/_meta/path/'))
from PathIni import PathIni
import shutil
import collections
from CommandToTemplate import CommandToTemplate
from ProjectName import ProjectName

class Pj:
    def __init__(self, args:list):
        self.__args = args
        self.__path_dir_target = PathIni()['work_flow_pj']
        pathlib.Path(self.__path_dir_target).mkdir(parents=True, exist_ok=True)

    def Run(self):
        return CommandToTemplate(self.__args).To()
        #return shutil.copytree(CommandToTemplate(self.__args).Path, os.path.join(self.__path_dir_target, ProjectName().Generate(args[1])))
        
    def GetName(self):
        pass
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2: raise Exception('引数不足です。ファイル拡張子をください。')
    sys.stdout.flush()
    #Pj(sys.argv[1:]).Run()
    print(Pj(sys.argv[1:]).Run())
