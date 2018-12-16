import csv

characters = open('csv/characters.csv', 'r')
paragraphs = open('csv/paragraphs.csv', 'r')
works = open('csv/works.csv', 'r')
scenes = open('csv/scenes.csv', 'r')

non_normal_out = open('csv/non_normal.csv', 'w+', newline='')

character_map = {}
scene_map = {}

work_reader = csv.DictReader(works)
scene_reader = csv.DictReader(scenes)
character_reader = csv.DictReader(characters)
paragraph_reader = csv.DictReader(paragraphs)

def add_prefix_to_dict(p: str, d: dict):
    return {f'{p}_{k}': v for k, v in d.items() if k != 'id'}

work_map = {row['id']: add_prefix_to_dict('work', row) for row in work_reader}
scene_map = {row['id']: add_prefix_to_dict('scene', row) for row in scene_reader}
character_map = {row['id']: add_prefix_to_dict('character', row) for row in character_reader}

output_fieldnames = [
    'paragraph_num',
    'text',
    *character_map['1'].keys(),
    *scene_map['1'].keys(),
    *work_map['1'].keys()   
]

output_fieldnames.remove('scene_work_id')

output_writer = csv.DictWriter(non_normal_out, fieldnames=output_fieldnames)

output_writer.writeheader()

for row in paragraph_reader:
    del row['id']
    character_id = row['character_id']
    character = character_map[character_id]
    row.update(character)
    del row['character_id']

    scene_id = row['scene_id']
    scene = scene_map[scene_id]
    row.update(scene)
    del row['scene_id']

    work_id = scene['scene_work_id']
    work = work_map[work_id]
    row.update(work)
    del row['scene_work_id']

    output_writer.writerow(row)

