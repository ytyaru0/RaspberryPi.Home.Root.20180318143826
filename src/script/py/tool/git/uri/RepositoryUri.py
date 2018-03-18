from abc import ABCMeta, abstractmethod
import urllib.parse
import os.path

# Git Repo URI の作成と解読（以下2クラスの合併）
# https://github.com/ytyaru0/GitHub.Uploader.Pi3.Https.201803020700/blob/master/src/web/service/github/uri/Protocol.py
# https://github.com/ytyaru0/Shell.Github.Commiter.20180316160244/blob/master/src/GitConfigReader.py
class Protocol(metaclass=ABCMeta):
    def __init__(self):
        self._user = None
        self._repo = None
    @abstractmethod
    def IsProtocol(self, url): raise NotImplementedError()
    @abstractmethod
    def To(self, *args, **kwargs): raise NotImplementedError()
    @abstractmethod
    def From(self, *args, **kwargs): raise NotImplementedError()
class Https(Protocol):
    def __init__(self):
        super().__init__()
        self.__password = None
    def IsProtocol(self, url): return url.endswith('.git') and url.startswith('https://')
    def To(self, user, repo, password=None):
        scheme = 'https://'
        if password is None: domain = 'github.com'
        else: domain = user + ':' + password + '@' + 'github.com'
        return scheme + domain + '/' + user + '/' + repo + '.git'
    def From(self, url):
        # A. https://github.com/{user}/{repo}.git
        # B. https://${user}:${pass}@github.com/{user}/{repo}.git
        res = {}
        urls = urllib.parse.urlsplit(url)
        res['scheme'] = urls.scheme
        split = os.path.split(urls.path)
        res['user'] = os.path.dirname(urls.path)[1:]
        res['repo'] = os.path.splitext(os.path.basename(urls.path))[0]
        if '@' in urls.netloc:
            userpass, res['server'] = urls.netloc.split('@')
            user, res['pass'] = userpass.split(':')
        else: res['server'] = urls.netloc
        return res
class Ssh(Protocol):    
    def __init__(self):
        super().__init__()
        self.__service = None
        self.__host = None
        self.__port = None
    def IsProtocol(self, url): return (url.endswith('.git') and (url.startswith('git@') or url.startswith('ssh://')))
    def To(self, ssh_host, user_name, repo_name):
        #from database.Database import Database as Db
        #account = Db().Accounts['Accounts'].find_one(Username=user_name)
        #sshHostName = Db().Accounts['SshConfigures'].find_one(AccountId=account['Id'])['HostName']
        #return "git@{0}:{1}/{2}.git".format(sshHostName, user_name, repo_name)
        return "git@{}:{}/{}.git".format(ssh_host, user_name, repo_name)
    def From(self, url):
        res = {}
        if url.startswith('ssh://'):
            # B. ssh://git@github.com:22/kyanny/hello.git
            urls = urllib.parse.urlsplit(url)
            res['scheme'] = urls.scheme
            res['service'], res['host'] = urls.netloc.split('@')
            if ':' in res['host']:
                res['host'], res['port'] = res['host'].split(':')
            res['user'] = urls.path.split('/')[1]
            res['repo'] = urls.path.split('/')[2][:-1*len('.git')]
        else:
            # A. git@{SSH_HOST}:{user}/{repo}.git
            res['service'], other = url.split('@')
            res['host'], other = other.split(':')
            res['user'], res['repo'] = other.split('/')
            if res['repo'].endswith('.git'): res['repo'] = res['repo'][:-1*(len('.git'))]
        return res

class RepositoryUriMeta(type):
    def __new__(self, name, bases, attrs):
        attrs['_{}__Protocols'.format(name)] = [Https(), Ssh()]
        for protocol in attrs['_{}__Protocols'.format(name)]:
            attrs['To' + protocol.__class__.__name__] = getattr(protocol, 'To')
        return type('RepositoryUri', (object,), attrs)
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
class RepositoryUri(metaclass=RepositoryUriMeta):
    def From(self, url):
        for p in self.__Protocols:
            if p.IsProtocol(url): return p.From(url)
        raise Exception('プロトコル判別エラー。URLから通信プロトコルを判別できませんでした。: {}'.format(url))

