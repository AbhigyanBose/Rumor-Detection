import json
import os

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


path_rnr = main_directory+'/'+events[0]+'/'+r_nr[0]
total_mentions = 0
count = 0

for idx1, t_name in enumerate(os.listdir(os.getcwd()+'/'+path_rnr)):
    path_t = path_rnr + '/' + t_name
    filename = os.listdir(os.getcwd()+'/'+path_t+'/'+s_r[0])[0]
    source_id = ''
    with open(
            path_t + '/' + s_r[0] + '/' + filename) as f:
        j_data = json.load(f)
        source_id = j_data['user']['screen_name']

    for idx2, filename in enumerate(os.listdir(os.getcwd()+'/'+path_t+'/'+s_r[1])):
        with open(
                path_t + '/' + s_r[1] + '/' + filename) as f:
            j_data = json.load(f)
            response_id = j_data['user']['screen_name']
            mentions = j_data['entities']['user_mentions']
            number_of_mentions = len(mentions)
            total_mentions += number_of_mentions
    count += len(os.listdir(os.getcwd() + '/' + path_t + '/' + s_r[1]))

print(total_mentions/count)
