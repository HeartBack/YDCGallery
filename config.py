import json
import  os

CONFIG_PATH=os.path.expanduser('~')+"\\config"
def getConfig():
    try:
        all_the_text = open(CONFIG_PATH).read()
        #print(all_the_text)
        ret = json.loads(all_the_text)
    except Exception as e:
        print(e)
        ret = None
    return ret
def updateConfig(config):
    open(CONFIG_PATH, 'w').write(json.dumps(config))
def getRecURL():
    dict = getConfig()
    #print(dict)
    if dict is not None:
        return dict["LastUrl"].strip()
    else:
        return None