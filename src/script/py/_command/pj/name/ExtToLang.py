import sys, os.path, pathlib
sys.path.append(os.path.expanduser('~/root/_meta/path/'))
from PathIni import PathIni
import yaml

class ExtToLang:
    def __init__(self):
        self.__path_dir_this = pathlib.Path(__file__).parent
        self.__path_target = None
        #self.__path_target = os.path.join(PathIni()['root_db_meta_programming'], "languages.yml")

    def To(self, ext):
        #print(ext)
        if type(ext) != str: raise ValueError('引数extは拡張子を表す文字列にしてください。(実行環境や言語を表す短いテキスト) 例: py')
        
        filepath = self.__GetExt2LangTsvFile()
        if filepath is not None: return self.__GetExt2LangTsv(filepath, ext if ext[0] != '.' else ext.lstrip('.'))
        filepath = self.__GetTsvFile()
        if filepath is not None: return self.__GetFromTsv(filepath, ext if ext[0] != '.' else ext.lstrip('.'))
        filepath = self.__GetYamlFile()
        if filepath is not None: return self.__GetFromYaml(filepath, ext if ext[0] == '.' else '.' + ext)
        raise Exception('拡張子と言語名の紐付けを定義したファイルが存在しません。')

    def __GetExt2LangTsvFile(self):
        for f in [self.__path_dir_this / 'ext2lang.tsv']:
            if os.path.isfile(f): return f

    def __GetExt2LangTsv(self, path, ext):
        import csv
        with open(path) as f:
            for row in csv.reader(f, delimiter='\t'):
                if ext == row[0]: return row[1]

    # 応答1秒。yamlより早い
    def __GetFromTsv(self, path, ext):
        import csv
        with open(path) as f:
            for row in csv.reader(f, delimiter='\t'):
                if ext in row[1:]: return row[0]

    def __GetTsvFile(self):
        for f in [self.__path_dir_this / 'languages.tsv', self.__path_target]:
            if os.path.isfile(f): return f

    # なんと6秒もかかる。応答遅すぎ
    def __GetFromYaml(self, path, ext):
        if type(ext) != str: raise ValueError('引数extは拡張子を表す文字列にしてください。例: .py')
        if ext[0] != '.': ext = '.' + ext
        with open(path) as f:
            data = yaml.load(f)
            for key in data.keys():
                if 'extensions' in data[key]:
                    if ext in data[key]['extensions']: return key
    
    def __GetYamlFile(self):
        for f in [self.__path_dir_this / 'languages.yml', self.__path_target]:
            if os.path.isfile(f): return f


if __name__ == '__main__':
    c = ExtToLang()
    print(c.Get('.js'))
    print(c.Get('js'))
