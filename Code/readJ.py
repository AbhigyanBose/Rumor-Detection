import json
import csv
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
csvFile = open('charliehebdoTweetGraph(Mentions).csv', 'w', newline='')
csvWriter = csv.writer(csvFile)
for idx1, t_name in enumerate(os.listdir(os.getcwd()+'/'+path_rnr)):
    path_t = path_rnr + '/' + t_name
    print(t_name)
    filename = os.listdir(os.getcwd()+'/'+path_t+'/'+s_r[0])[0]
    source_id = ''
    with open(
            path_t + '/' + s_r[0] + '/' + filename) as f:
        j_data = json.load(f)
        # print(j_data)
        source_id = j_data['user']['id']
        #print(source_id)
    # print(filename)
    for idx2, filename in enumerate(os.listdir(os.getcwd()+'/'+path_t+'/'+s_r[1])):
        # print(str(idx2 + 1) + ': ' + filename)
        with open(
                path_t + '/' + s_r[1] + '/' + filename) as f:
            j_data = json.load(f)
            # print(j_data)
            response_id = j_data['user']['screen_name']
            # print(str(idx2+1) + ': ' + str(response_id))
            for mentions in j_data['entities']['user_mentions']:
                mention_id = mentions['screen_name']
                csvWriter.writerow([response_id, mention_id, '1'])
                print(str(idx2 + 1) + ': ' + str(response_id)+'  '+str(mention_id))

csvFile.close()