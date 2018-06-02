import json

with open(
        '../Datasets/phemernrdataset/pheme-rnr-dataset/charliehebdo/rumours/552783238415265792/source-tweet/552783238415265792.json') as f:
    j_data = json.load(f)
    print(j_data)
    print(j_data['user'])
