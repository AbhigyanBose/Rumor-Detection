import json
import csv
import os


def alter_text(text):
    new_text = ''
    for word in text.split():
        if word[0] == '#' or word[0] == '@':
            word = word[0]
        if word.startswith('http') or word.startswith('www'):
            word = 'http-link'
        new_text = new_text+' '+word
    return new_text


dataset = '/home/abhigyan/Documents/Rumor Detection/Datasets/phemerumourschemedataset/pheme-rumour-scheme-dataset/threads/en'
r_list = ''
s_r = ['source-tweets', 'reactions']

# with open(
#         path+'/'+file) as f:
#     j_data = json.load(f)
#     #print(j_data)
#     user_data = j_data['user']
#     print(user_data['id'])

source_file = open("source.csv", "w+")
dest_file = open("destination.csv", "w+")
source_type_dict = {'supporting':'0', 'denying':'1', 'underspecified':'2'}
destination_type_dict = {'agreed':'0', 'disagreed':'1', 'appeal-for-more-information':'2', 'comment':'3'}
all_dict = {}
source_dict = {}
response_dict = {}
text = ''
t_id = 0
t_type = ''

with open('dict_file.csv', mode='r') as infile:
    reader = csv.reader(infile)
    all_dict = {rows[0]: rows[1] for rows in reader}

# for a in all_dict:
#     print(a,all_dict[a])

for event in os.listdir(dataset):
    # print(event)
    for idx1, t_name in enumerate(os.listdir(dataset+'/'+event)):
        path_t = dataset + '/' + event + '/' + t_name
        filename = os.listdir(path_t + '/' + s_r[0])[0]
        with open(
                path_t + '/' + s_r[0] + '/' + filename) as f:
            j_data = json.load(f)
            t_id = j_data['id']
            text = j_data['text']
            text = alter_text(text)
            # print(t_id)
            # print(path_t + '/' + s_r[0] + '/' + filename)
            t_type = all_dict[str(t_id)]
            # print(t_type)
            source_dict[t_type] = text
            source_file.write(source_type_dict[t_type]+','+text[1:]+'\n')
            # print(text)
        for idx2, filename in enumerate(os.listdir(path_t + '/' + s_r[1])):
            with open(
                    path_t + '/' + s_r[1] + '/' + filename) as f:
                try:
                    j_data = json.load(f)
                    t_id = j_data['id']
                    # print(t_id)
                    text = j_data['text']
                    text = alter_text(text)
                    t_type = all_dict[str(t_id)]
                    # print(t_type)
                    response_dict[t_type] = text
                    dest_file.write(destination_type_dict[t_type]+','+text[1:]+'\n')
                    # print(text)
                    continue
                except KeyError:
                    print('KeyError')


dest_file.close()
source_file.close()