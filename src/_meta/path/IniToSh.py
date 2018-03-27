import configparser
import pathlib
import os
import re

class IniToSh:
    def __init__(self):
        #self.__path_root = pathlib.Path('~/root/db/path/')
        #self.__path_root = pathlib.Path('~/root/_meta/path/')
        #self.__path_root = pathlib.Path('/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/')
        self.__path_root = pathlib.Path(__file__).parent

    def To(self):
        paths_ini = [p for p in (self.__path_root / 'ini').glob('*.ini')]
        path_sh = self.__path_root / 'sh' / 'paths.sh'
        path_sh.parent.mkdir(parents=True, exist_ok=True)
        if not self.__ShouldWrite(paths_ini, path_sh): return
        self.__WriteSh(paths_ini, path_sh, 'Paths')
 
    # shが無いかiniより古ければ書き込むべき
    def __ShouldWrite(self, paths_ini, path_sh):
        if not path_sh.is_file(): return True
        for ini in paths_ini:
            if os.stat(path_sh).st_mtime < os.stat(ini).st_mtime: return True
        return False
       
    def __WriteSh(self, paths_ini, path_sh, section):
        data = "declare -A {}".format(section) + '\n'
        for path_ini in paths_ini:
            parser = configparser.ConfigParser()
            parser.read(path_ini)
            #for key in sorted(parser[section]):
            for key in parser[section]:
                value = self.__ReplaceVarToArray(section, parser[section][key])
                data += "{}[\"{}\"]=\"{}\"".format(section, key, value) + '\n'
        with path_sh.open('w') as f: f.write(data)

    def __ReplaceVarToArray(self, section, value):
        def re_sub_replace(match):
            if match.group(0).startswith('${'):
                result = match.group(0)
                if result.startswith('${'): result = result[2:]
                if result.endswith('}'): result = result[:-1]
                return '${' + section + '[' + result + ']}'

        return re.sub(r'(\${[^}]+})', re_sub_replace, value)


if __name__ == '__main__':
    IniToSh().To()
