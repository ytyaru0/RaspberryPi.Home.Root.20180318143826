import pathlib
import configparser
class PathIni:
    def __init__(self): self.__Initialize()
    def __getitem__(self, key): return self.Get(key)
    def Get(self, key): return pathlib.Path(self.__parser[self.__section][key]).expanduser()
    @property
    def Keys(self): return self.__parser[self.__section].keys()
    @property
    def Parser(self): return self.__parser
    @property
    def FilePath(self): return self.__path_ini

    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

    def __Initialize(self):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent
        self.__path_ini = self.__path_dir_root / 'ini/paths.ini'
        self.__section = 'Paths'
        self.__Load()
 
    def __Load(self):
        self.__parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.__parser.read(self.__path_ini)
        return sorted(self.__parser[self.__section])


print(PathIni()['work'])

