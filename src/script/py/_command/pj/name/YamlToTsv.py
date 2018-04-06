import sys, os.path, pathlib
sys.path.append(os.path.expanduser('~/root/_meta/path/'))
from PathIni import PathIni
import yaml
import io

class YamlToTsv:
    def __init__(self):
        self.__path_dir_target = pathlib.Path(__file__).parent
        self.__path_target = None
        #self.__path_target = os.path.join(PathIni()['root_db_meta_programming'], "languages.yml")

    def To(self):
        with io.StringIO() as buf:
            for key, exts in self.__Yaml():
                buf.write(self.__TsvRecord(key, exts))
            with open(self.__path_dir_target / 'languages.tsv', 'w') as f:
                f.write(buf.getvalue())
        #with open(self.__GetFile()) as f:
        #    data = yaml.load(f)
        #    for key in data.keys():
        #        if 'extensions' in data[key]:
        #            buf.write(self.__TsvRecord(key, data[key]['extensions']))
                
    def __Yaml(self):
        with open(self.__GetFile()) as f:
            data = yaml.load(f)
            for key in data.keys():
                if 'extensions' in data[key]: yield key, data[key]['extensions']
         
    def __GetFile(self):
        for f in ['/tmp/work/Python.ProjectMaker.20180402173000/src/languages.yml', self.__path_dir_target / 'languages.yml', self.__path_target]:
            if os.path.isfile(f): return f

    def __TsvRecord(self, key, extensions):
        return key + '\t' + '\t'.join([e.lstrip('.') for e in extensions]) + '\n'

    
if __name__ == '__main__':
    c = YamlToTsv()
    c.To()
