import pathlib
import configparser
class PathIni:
    def __init__(self):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent
        self.__path_ini = self.__path_dir_root / 'ini/paths.ini'
    
    def Load(self):
        p = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        p.read(self.__path_ini)
        print(type(p['Paths']))
        return sorted(p['Paths'])
        #return p['Paths']

    @property
    def FilePath(self): return self.__path_ini
