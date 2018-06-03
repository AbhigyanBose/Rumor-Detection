import json

path = '../Datasets/phemernrdataset/pheme-rnr-dataset/charliehebdo/rumours/552783238415265792/source-tweet'
file = '552783238415265792.json'
with open(
        path+'/'+file) as f:
    j_data = json.load(f)
    #print(j_data)
    user_data = j_data['user']
    print(user_data['id'])
