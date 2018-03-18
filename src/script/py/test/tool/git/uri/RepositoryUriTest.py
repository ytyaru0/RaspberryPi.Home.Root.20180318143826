# RepositoryUri.py を参照するため
#import sys,os
#sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),'tool/git/config'))
import sys, pathlib
sys.path.append(str(pathlib.Path(pathlib.Path(__file__).parent.parent.parent.parent.parent, 'tool/git/uri')))

import unittest
from RepositoryUri import RepositoryUri
class RepositoryUriTest(unittest.TestCase):
    def test_has_attr(self):
        self.assertTrue(hasattr(RepositoryUri(), 'ToHttps'))
        self.assertTrue(hasattr(RepositoryUri(), 'ToSsh'))
        self.assertTrue(hasattr(RepositoryUri(), 'From'))

    def test_to_https_A(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        self.assertEqual("https://github.com/{}/{}.git".format(user, repo), RepositoryUri().ToHttps(user, repo))
    def test_to_https_B(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        pw = 'PASS_WORD'
        self.assertEqual("https://{0}:{2}@github.com/{0}/{1}.git".format(user, repo, pw), RepositoryUri().ToHttps(user, repo, pw))
    def test_to_ssh_A(self):
        host = 'ytyaru0.github.com'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        self.assertEqual("git@{}:{}/{}.git".format(host, user, repo), RepositoryUri().ToSsh(host, user, repo))

    def test_from_https_A(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "https://github.com/{}/{}.git".format(user, repo)
        res = RepositoryUri().From(url)
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
    def test_from_https_B(self):
        user = 'ytyaru0'
        repo = 'MyRepoName'
        pw = 'PASS_WORD'
        url = "https://{0}:{2}@github.com/{0}/{1}.git".format(user, repo, pw)
        res = RepositoryUri().From(url)
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertTrue('pass' in res.keys())
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
        self.assertEqual(pw, res['pass'])

    def test_from_ssh_A(self):
        host = 'ytyaru0.github.com'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "git@{}:{}/{}.git".format(host, user, repo)
        res = RepositoryUri().From(url)
        self.assertTrue('host' in res.keys())
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(host, res['host'])
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
    def test_from_ssh_B1(self):
        host = 'ytyaru0.github.com'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "ssh://git@{}/{}/{}.git".format(host, user, repo)
        res = RepositoryUri().From(url)
        self.assertTrue('host' in res.keys())
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(host, res['host'])
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])
    def test_from_ssh_B2(self):
        host = 'ytyaru0.github.com'
        port = '22'
        user = 'ytyaru0'
        repo = 'MyRepoName'
        url = "ssh://git@{}:{}/{}/{}.git".format(host, port, user, repo)
        res = RepositoryUri().From(url)
        self.assertTrue('host' in res.keys())
        self.assertTrue('port' in res.keys())
        self.assertTrue('user' in res.keys())
        self.assertTrue('repo' in res.keys())
        self.assertEqual(host, res['host'])
        self.assertEqual(port, res['port'])
        self.assertEqual(user, res['user'])
        self.assertEqual(repo, res['repo'])


if __name__ == '__main__':
    unittest.main()
