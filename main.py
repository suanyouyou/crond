import time
import itchat

def crond():
    cronds=dict()
    n = 0
    with open("crond.txt", 'r', encoding='utf-8') as f:
        #f.readlines是列表
        for line in f.readlines():
        #rstrip去掉右边非字符
            linestr=line.strip()
            linestr=linestr.replace('月','-')
            linestr=linestr.replace('日','')
            cronds[n]={'time':linestr[:11].rstrip(),'content':linestr[11:]}
            n += 1
    return cronds
print(crond())
# print(time)

#设定一天计时器
daysec=24*60*60
def exec():
    get_time=time.strftime('%m-%d',time.localtime())
    for n in range(len(crond())):
        if get_time[:5]==crond()[n]['time'][:5]:
            contents='时间：%s 任务：%s'%(crond()[n]['time']  ,crond()[n]['content']   )
            itchat.send(contents,'filehelper')
    #开始计时
    time.sleep(daysec)
    exec()

if __name__=="__main__":
    itchat.auto_login(hotReload=True)
    exec()



