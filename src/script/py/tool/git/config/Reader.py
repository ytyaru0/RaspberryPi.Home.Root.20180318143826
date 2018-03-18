# RepositoryUri.py を参照するため
import sys, pathlib
sys.path.append(str(pathlib.Path(pathlib.Path(__file__).parent.parent, 'uri')))
import configparser
from RepositoryUri import RepositoryUri
class Reader:
    def __init__(self, path):
        self.__config = configparser.ConfigParser()
        self.__config.read(path)
    @property
    def RemoteOriginUrl(self): return self.__config['remote "origin"']['url']
    @property
    def RemoteOriginRepo(self): return RepositoryUri().From(self.RemoteOriginUrl)['repo']
    @property
    def RemoteOriginUser(self): return RepositoryUri().From(self.RemoteOriginUrl)['user']


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2: raise Exception('ArgumentError: 引数が足りません。.gitディレクトリがあるディレクトリパスを渡してください。: {}'.format(sys.argv))
    import os.path
    git_config = os.path.join(sys.argv[1], '.git', 'config')
    if not os.path.isfile(git_config): raise Exception('ArgumentError: .git/config ファイルが存在しません。: {}'.format(git_config))
    from Reader import Reader
    reader = Reader(git_config)
    # "user repo"
    print(reader.RemoteOriginUser, reader.RemoteOriginRepo)

