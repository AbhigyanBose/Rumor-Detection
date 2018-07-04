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


main_directory = '../Datasets/phemernrdataset/pheme-rnr-dataset'
events = ['charliehebdo', 'ferguson', 'germanwings-crash', 'ottawashooting', 'sydneysiege']
r_nr = ['rumours', 'non-rumours']
r_list = ''
s_r = ['source-tweet', 'reactions']

# with open(
#         path+'/'+file) as f:
#     j_data = json.load(f)
#     #print(j_data)
#     user_data = j_data['user']
#     print(user_data['id'])

text_file = open("l_model_data", "w+")

for event_no in range(0, 5):
    for rnr_no in range(0, 2):
        path_rnr = main_directory + '/' + events[event_no] + '/' + r_nr[rnr_no]

        for idx1, t_name in enumerate(os.listdir(os.getcwd() + '/' + path_rnr)):
            path_t = path_rnr + '/' + t_name
            filename = os.listdir(os.getcwd() + '/' + path_t + '/' + s_r[0])[0]
            text = ''
            with open(
                    path_t + '/' + s_r[0] + '/' + filename) as f:
                j_data = json.load(f)
                text = j_data['text']
                text = alter_text(text)
                text_file.write(text+'\n')
                # print(text)

            for idx2, filename in enumerate(os.listdir(os.getcwd() + '/' + path_t + '/' + s_r[1])):
                with open(
                        path_t + '/' + s_r[1] + '/' + filename) as f:
                    j_data = json.load(f)
                    text = j_data['text']
                    text = alter_text(text)
                    text_file.write(text + '\n')
                    # print(text)


text_file.close()