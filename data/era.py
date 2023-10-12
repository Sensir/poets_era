import json
import random
with open('in.csv', 'r') as f:
    data = [[], []]
    index = 0
    i = 0
    part_2 = False
    gap = 5
    for line in f:
        line = line.replace(' ', '').strip()
        if line.startswith('#'):continue
        items = line.split(',')
        born = int(items[2])
        gone = int(items[3])
        half = (gone - born + 1)//2
        if items[0] == '宋' and not part_2:
            i = 0
            index = 1
            part_2 = True
        i += 1
        data[index].append(
            {
                'coords': [
                    [gone, i*gap],
                    [born, i*gap]
                ],
                'label' : f'{items[1]} [{items[0]}] {items[2]}-{items[3]}'
            }
            )

    json_array = json.dumps(data, ensure_ascii=False, indent=2)

    with open('../data.js', 'w') as js:
        js.write(f'''var data = {json_array};''')