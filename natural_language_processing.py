import jieba
def Initialization():
    jieba.suggest_freq('采购单', True)
    jieba.suggest_freq('采购提交', True)
    jieba.suggest_freq('玻尿酸', True)
    jieba.suggest_freq("新增采购", True)
    jieba.suggest_freq("水泥",True)
    jieba.del_word('采购提交水泥')
def NLP(string):
    Initialization()
    NLPlist = jieba.lcut(string.replace('的', ''))
    if len(NLPlist) > 4:
         NLPlist[-2] = NLPlist[-2]+NLPlist[-1]
    return NLPlist
