import sys, os.path, pathlib
import shlex, shutil
#import jinja2
#from jinja2 import Template, Environment, FileSystemLoader, meta
import string
from CommandsFile import CommandsFile
import datetime
sys.path.append(os.path.expanduser('~/root/_meta/path/'))
from PathIni import PathIni
from name.ProjectName import ProjectName
from name.Command import Command
from TemplateRenderer import TemplateRenderer

class CommandToTemplate:
    def __init__(self, commands:list):
        self.__commands = commands
        self.__cmdfile = CommandsFile()
        self.__tpl_var_prefix = '-'
    
    def To(self):
        categolies, tpl_var_dict = Command().Analize(self.__commands)
        path_tpl = self.__cmdfile.TemplateDir / self.__CommandToTemplatePath(categolies)
        path_target = PathIni()['work_flow_pj'] / ProjectName().Generate(self.__commands)
        shutil.copytree(path_tpl, path_target)
        if (path_target / '__TEMPLATE__').is_file(): os.remove(path_target / '__TEMPLATE__')
        if (path_target / '__DEFAULT__').is_file(): os.remove(path_target / '__DEFAULT__')

        if 'filename' in tpl_var_dict: filename = tpl_var_dict['filename']
        elif '_1' in tpl_var_dict: filename = tpl_var_dict['_1']
        elif '_0' in tpl_var_dict: filename = tpl_var_dict['_0']
        else: filename = '{{filename}}'
        
        # パス名 {{filename}}置換
        for p in path_target.glob('**/*{{filename}}*'):
            fn = p.name.replace('{{filename}}', filename)
            p.rename(p.parent / fn)

        for p in path_target.glob('**/*'):
            if p.is_file() and not p.is_symlink():
                res = TemplateRenderer().Render(p, filename=filename)
                with p.open(mode='w') as f:
                    f.write(res)
        """       
        # ファイル内容 {{filename}}置換
        for p in path_target.glob('**/*'):
            if p.is_file() and not p.is_symlink():
                env = Environment(loader=FileSystemLoader(str(path_target)))
                template = env.get_template(p.relative_to(path_target), p)
                template.globals['now'] = datetime.datetime.now()
                with p.open(mode='w') as f:
                    f.write(template.render(filename=filename))
        """
        return path_target
        """
        env = Environment(loader=FileSystemLoader(str(self.__cmdfile.TemplateDir)))
        template = env.get_template(path)
        template.globals['now'] = datetime.datetime.now()
        TemplateVarsErrorChecker(self.__tpl_var_prefix, tpl_var_dict, env, template).IsExists()
        try:
            return template.render(**tpl_var_dict)
        except:
            import traceback
            traceback.print_exc()
            self.__GetIncludeFilesCandidateMessage(categolies, env, template)
            #raise e
            import sys
            sys.exit(1)
        """

    def __CommandToTemplatePath(self, categolies:list):
        input_command = ' '.join([a for a in categolies]).strip()
        for d in self.__cmdfile.Load():
            for c in d.commands:
                if c == input_command:
                    return d.path
        raise Exception('コマンドに対応するテンプレートファイルパスが見つかりません。\n  command=\'{}\'\n  参照ファイル:{}'.format(' '.join(self.__commands), self.__cmdfile.FilePath))
    """
    def __GetIncludeFilesCandidateMessage(self, categolies:list, env:jinja2.Environment, template:jinja2.Template):
        with pathlib.Path(template.filename).open() as f:
            source = f.read()
            includes = TemplateIncludeFiles(self.__cmdfile.TemplateDir, env).Get(source)
            print('****************************************')
            print('テンプレート変数が不足しているか誤りがあります。')
            print('たとえば以下のように入力してください。\n')
            tpl_var_names = sorted(meta.find_undeclared_variables(env.parse(source)), key=str.lower)
            print('$ do', ' '.join(categolies), self.__GetExampleCommand(tpl_var_names, includes) + '\n')
            print('テンプレート変数は以下のコマンドで指定します。')
            print(' '.join([self.__tpl_var_prefix + v for v in tpl_var_names ]) + '\n')
            if 0 < len(includes):
                print('include用テンプレ引数とその値の候補は以下のとおり。')
                for i in includes:
                    print(self.__tpl_var_prefix+i[0], i[1])
            print('\n対象テンプレートは以下です。')
            print(template.filename)
            print('****************************************')

    def __GetExampleCommand(self, tpl_var_names, includes):
        command = ''
        inc_names = [i[0] for i in includes]
        for n in tpl_var_names:
            if n in inc_names: continue
            command += self.__tpl_var_prefix + n + ' A '
        for i in includes:
            command += self.__tpl_var_prefix + i[0] + ' ' + i[1][0] + ' '
        return command
    """ 
"""
class TemplateVarsErrorChecker:
    def __init__(self, prefix, tpl_var_dict, env, template):
        self.__prefix = prefix
        self.__tpl_var_dict = tpl_var_dict
        self.__env = env
        self.__template = template
        self.__tpl_var_names = None
        self.__LoadTemplateVars()

    def __LoadTemplateVars(self):
        if self.__tpl_var_names is not None: return
        with pathlib.Path(self.__template.filename).open() as f:
            source = f.read()
            self.__tpl_var_names = sorted(jinja2.meta.find_undeclared_variables(self.__env.parse(source)), key=str.lower)

    def IsExists(self):
        not_exists = []
        if 0 == len(self.__tpl_var_dict.keys()): not_exists = list(self.__tpl_var_names)
        else:
            for key in self.__tpl_var_names:
                if key not in self.__tpl_var_dict.keys(): not_exists.append(key)
        #for key in self.__tpl_var_dict:
        #    if key not in self.__tpl_var_names: not_exists.append(key)
        if 0 < len(not_exists):
            msg = '以下のテンプレート変数が不足しています。\n{}'.format(not_exists)
            for key in not_exists:
                if key.startswith('_') and key[len(self.__prefix):].isdigit():
                    msg += '\n\n' + self.__GetPositionalVarsHelp()
                    break
            #raise Exception(msg)
            #raise TemplateVarsErrorChecker.NotExistTemplateVars(msg)
            raise self.NotExistTemplateVars(msg)

    def __GetPositionalVarsHelp(self):
        msg = '位置引数について\n\n'
        msg += '  "_数値" の名前のテンプレ変数は、位置引数です。テンプレ変数をコマンドで指定開始した位置が自動的に名前になります。\n'
        msg += '  たとえば以下のようにすると、テンプレ変数"_0"に"MyClass"をセットしたことになります。\n'
        msg += '  $ do py -MyClass\n'
        msg += '  以下のように変数名を入力せず値だけで済むため少し楽です。\n'
        msg += '  $ do py -_0 MyClass\n'
        msg += '  $ do py -ClassName MyClass'
        return msg

    class NotExistTemplateVars(Exception): pass



# -V -V -V
# -" -V" -V
# -K V -K V
# -K "-V" -K V
# -V -V -V -K V -V -K V
# Key: -[_a-zA-Z][_a-zA-Z0-9]。テンプレ変数名と同一。重複したら後者で上書き。
# Value: スペースやハイフンを使うときはクォーテーションで囲む。
class TemplateVarsArgumentAnalizer:
    def __init__(self, tpl_var_prefix):
        self.__tpl_var_prefix = tpl_var_prefix
    @property
    def Prefix(self): return self.__tpl_var_prefix

    # tpl_vars: shlex.split()済みで先頭に`-`がある要素以降すべて
    def Analize(self, commands:list):
        categolies, tpl_vars = self.__SplitCategolyAndTemplateVars(commands)
        return categolies, self.__MakeTemplateVarsDict(tpl_vars)

    # コマンド文字列をカテゴリとテンプレ変数に分離する
    # command: $ do {categoly} ... -{tpl_var} ... 
    def __SplitCategolyAndTemplateVars(self, commands:list):
        for i, a in enumerate(commands):
            if a.startswith(self.Prefix): return commands[:i], commands[i:]
        return commands, []

    def __MakeTemplateVarsDict(self, tpl_vars):
        tpl_var_dict = {}
        position = 0 # 位置引数カウンタ
        for i, v in enumerate(tpl_vars):
            if self.IsPositional(tpl_vars, i):
                tpl_var_dict['_'+str(i)] = self.UnQuote(v[1:])
                position += 1
            else:
                if not self.IsLast(tpl_vars, i):
                    tpl_var_dict[v[1:]] = self.UnQuote(tpl_vars[i+1])
        return tpl_var_dict

    def IsPrefix(self, arg): return arg.startswith(self.Prefix)
    def IsLiteral(self, arg):
        if arg.startswith('\'') and arg.endswith('\''): return True
        elif arg.startswith('"') and arg.endswith('"'): return True
        else: return False
    def UnQuote(self, arg):
        if self.IsLiteral(arg): return arg[1:-1].replace('\\', '')
        else: return arg
    def IsPositional(self, tpl_vars:list, start:int):
        if self.IsLast(tpl_vars, start): return self.IsPrefix(tpl_vars[start])
        if self.IsPrefix(tpl_vars[start]) and self.IsPrefix(tpl_vars[start+1]):
            return True
        return False
    def IsLast(self, tpl_vars:list, index:int):
        if index+1 == len(tpl_vars): return True
        else: return False

class TemplateIncludeFiles:
    def __init__(self, tpl_dir:pathlib.Path, env:jinja2.Environment):
        self.__tpl_dir = tpl_dir
        self.__env = env

    def Get(self, source:str):
        token_gen = self.__env.lex(self.__env.preprocess(source))
        tokens = list(token_gen)
        return sorted(self.GetIncludeCandidates(tokens, self.GetBlockContentIndices(tokens)), key=lambda i: i[0].lower())
           
    def GetBlockContentIndices(self, tokens):
        block_indices = []
        start = -1
        for i, t in enumerate(tokens):
            if -1 != start:
                if t[1] == 'block_end':
                    block_indices[-1][1] = i
                    start = -1
                    continue
            else:
                if t[1] == 'block_begin':
                    start = i 
                    block_indices.append([start, -1])
                    continue
        return block_indices

    def GetIncludeCandidates(self, tokens, block_indices):
        values = []
        for rng in block_indices:
            start = rng[0] + self.GetIncludeValueInde(tokens[rng[0]:rng[1]])
            if -1 == start: continue
            values.append(self.GetIncludeValuePattern(tokens[start+1:rng[1]-1]))
        return values

    def GetIncludeValueInde(self, block_tokens):
        for i, token in enumerate(block_tokens):
            if token[1] == 'name':
                # {% block で見つかった最初の name構文 の値が include なら真
                if token[2] == 'include': return i
                # {% block では 変数なども name構文である。includeという名の変数もありうるが、最初にきているかどうかで変数かどうか判断できる
                else: return -1
        return -1

    def GetIncludeValuePattern(self, include_value_tokens:list):
        name = None
        value = ''
        for i, token in enumerate(include_value_tokens):
            if 'string' == token[1]: value += token[2][1:-1]
            elif 'name' == token[1]:
                if name is None:
                    name = token[2]
                    value += '**/*'
                else: raise Exception('includeブロック {% include %} の値に2つ以上の テンプレ変数 {{}} を使っています。ひとつだけにしてください。')
        return name, self.__GetPatternValues(value)

    def __GetPatternValues(self, pattern):
        pattern_parent = pathlib.PurePath(pattern).parent.parent
        pattern_full = self.__tpl_dir / pattern_parent
        values = []
        for path in self.__tpl_dir.glob(pattern):
            p = path.relative_to(pattern_full)
            values.append(str(p.parent / p.stem))
        return sorted(values, key=str.lower)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3: raise Exception('起動引数エラー。コマンド文字列と出力先ファイルのフルパスをください。')
    c = CopyTemplate(sys.argv[1:-1], sys.argv[-1])
    c.Copy()
"""
