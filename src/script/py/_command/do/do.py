import sys, pathlib
sys.path.append('~/root/_meta/path/')
from PathIni import PathIni
sys.path.append(PathIni()['root_script_py']  / 'os/file/'target)
from SequenceName import SequenceName
import collections
from CommandToTemplate import CommandToTemplate

class Do:
    def __init__(self, args:list):
        self.__args = args
        self.__path_dir_target = PathIni()['work_flow_do']
        pathlib.Path(self.__path_dir_target).mkdir(parents=True, exist_ok=True)

    def Run(self):
        name = SequenceName(self.__path_dir_target, self.__args[0], radix=36, is_alignment=True).Generate()
        filepath = pathlib.Path(self.__path_dir_target) / (name + '.' + self.__args[0])
        with filepath.open('x') as f:
            f.write(CommandToTemplate(self.__args).To())
            return str(filepath)
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2: raise Exception('引数不足です。ファイル拡張子をください。')
    sys.stdout.flush()
    print(Do(sys.argv[1:]).Run())
