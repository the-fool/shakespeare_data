import csv
import pickle

chapters = open('chapters.csv', 'r')
chapt_out = open('chapter_out.csv', 'w+', newline='')
paragraph_in = open('paragraphs.csv', 'r')
paragraph_out = open('paragraphs_out.csv', 'w+', newline='')

id_map = {}
start = 1

chap_reader = csv.DictReader(chapters)
para_reader = csv.DictReader(paragraph_in)
chap_writer = csv.DictWriter(chapt_out, fieldnames=['id', 'act','scene','description','work_id'])
para_writer = csv.DictWriter(paragraph_out, fieldnames=['id', 'paragraph_num', 'text', 'character_id', 'scene_id'])

# do chapter conversion
chap_writer.writeheader()
for row in chap_reader:
    old_id = row['id']
    id_map[old_id] = start
    row['id'] = start
    chap_writer.writerow(row)
    start += 1

# checkpoint
with open('kv.pickle', 'wb') as handle:
    pickle.dump(id_map, handle, protocol=pickle.HIGHEST_PROTOCOL)

# convert paragraphs
para_writer.writeheader()
for row in para_reader:
    scene_id = row['scene_id']
    new_id = id_map[scene_id]
    row['scene_id'] = new_id
    para_writer.writerow(row)





