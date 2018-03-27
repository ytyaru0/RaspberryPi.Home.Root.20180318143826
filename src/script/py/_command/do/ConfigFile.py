import pathlib
import os.path
import csv
class ConfigFile:
    def __init__(self, file_name):
        self.__path_dir_root = pathlib.Path(__file__).resolve().parent.parent
        self.__path_dir_res = self.__path_dir_root / 'res'
        if file_name.endswith('.tsv'): self.__file_name = file_name
        else: self.__file_name = file_name + '.tsv'
        #self.__GetDefaultPath()
        self.__LoadFilePath()
        self.__LoadTemplateDir()
    
    @property
    def FilePath(self): return self.__path_file_this
    @property
    def TemplateDir(self): return self.__path_dir_template
    @property
    def DefaultFilePath(self): return self.__GetDefaultPath()
    #def DefaultFilePath(self): return self.__path_dir_res / self.__file_name

    def __LoadFilePath(self):
        work_paths = self.__LoadMetaPath('work')
        self.__path_file_this = pathlib.Path(work_paths['work_meta_command_do']) / self.__file_name
        self.__path_file_this.parent.mkdir(parents=True, exist_ok=True)

    def __LoadTemplateDir(self):
        root_paths = self.__LoadMetaPath('root')
        self.__path_dir_template = pathlib.Path(root_paths['root_db_template']) / self.__file_name
        if not self.__path_dir_template.is_dir():
            self.__path_dir_template = self.__path_dir_res

    def __LoadMetaPath(self, file_name):
        path_config = self.__GetMetaPath(file_name)
        import configparser
        p = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        p.read(path_config)
        return p['Paths']

    def __GetMetaPath(self, file_name):
        paths = ['~/root/_meta/_meta/path/ini/', 
            '/tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/ini/']
        for path in paths:
            path = pathlib.Path(path) / '{}.ini'.format(file_name)
            if path.is_file(): return path
        raise Exception('{}.iniファイルが存在しません。次のいずれかのディレクトリ配下に作成してください'.format(file_name))
        return None

    def __GetDefaultPath(self):
        paths = [self.__LoadMetaPath('root')['root_db_template'], self.__path_dir_root / 'config', self.__path_dir_root, self.__path_dir_res]
        for path in paths:
            p = path / self.__file_name
            if p.is_file(): return p
        raise Exception('{} デフォルトファイルが存在しません。次のパス配下に作成してください。'.format(self.__file_name, paths))

    def LoadTsv(self):
        with self.__path_file_this.open() as f:
            tsv = csv.reader(f, delimiter='\t')
            for columns in tsv:
                if 1 == len(columns) and 0 == len(columns[0].strip()): continue
                if columns[0].strip().startswith('#'): continue
                yield columns

"""
if __name__ == '__main__':
    c = ConfigFile('commands')
    print(c.FilePath)
    print(c.TemplateDir)

    c = ConfigFile('command_replace')
    print(c.FilePath)
    print(c.TemplateDir)
"""

