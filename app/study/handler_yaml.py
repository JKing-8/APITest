import yaml
with open('./my_yaml01.yml','r',encoding='utf-8') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    print(data)
    print(data['url'])
    print(data['ip'])

with open('./my_yaml02.yml','r') as f:
    data2 = yaml.load(f,Loader=yaml.FullLoader)
    print(data2)

with open('./my_yaml03.yml', 'r') as f:
    data3 = yaml.load(f, Loader=yaml.FullLoader)
    print(data3)