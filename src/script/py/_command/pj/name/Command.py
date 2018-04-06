import pathlib
import shlex
import datetime
# -V -V -V
# -" -V" -V
# -K V -K V
# -K "-V" -K V
# -V -V -V -K V -V -K V
# Key: -[_a-zA-Z][_a-zA-Z0-9]。テンプレ変数名と同一。重複したら後者で上書き。
# Value: スペースやハイフンを使うときはクォーテーションで囲む。
class Command:
    def __init__(self, tpl_var_prefix='-'):
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
            if self.__IsPositional(tpl_vars, i):
                tpl_var_dict['_'+str(i)] = self.__UnQuote(v[1:])
                position += 1
            else:
                if not self.__IsLast(tpl_vars, i):
                    tpl_var_dict[v[1:]] = self.__UnQuote(tpl_vars[i+1])
        return tpl_var_dict

    def IsPrefix(self, arg): return arg.startswith(self.Prefix)
    def __IsLiteral(self, arg):
        if arg.startswith('\'') and arg.endswith('\''): return True
        elif arg.startswith('"') and arg.endswith('"'): return True
        else: return False
    def __UnQuote(self, arg):
        if self.__IsLiteral(arg): return arg[1:-1].replace('\\', '')
        else: return arg
    def __IsPositional(self, tpl_vars:list, start:int):
        if self.__IsLast(tpl_vars, start): return self.IsPrefix(tpl_vars[start])
        if self.IsPrefix(tpl_vars[start]) and self.IsPrefix(tpl_vars[start+1]):
            return True
        return False
    def __IsLast(self, tpl_vars:list, index:int):
        if index+1 == len(tpl_vars): return True
        else: return False
