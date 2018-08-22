## Read in the pascal voc file and potentially alter to csv for this?
import os
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

base_dir = '/Users/datascience4/Documents/training3'
print(len(os.listdir(base_dir)))
xml_files = os.listdir(base_dir)
print(xml_files)
items = []

for i in range(len(xml_files)):
    xml = os.path.join(base_dir, xml_files[i])
    tree = ET.parse(xml)
    root = tree.getroot()
    # path needs to be declared
    ## each row needs to look like this.
    ## path/to/img1.jpg xmin,ymin,xmax,ymax,class_id xmin,ymin,xmax,ymax,class_id
    ## path/to/img2.jpg xmin,ymin,xmax,ymax,class_id
    ## so each object in an image is only seperated by a space
    path = root.find('path').text
    ## make it a string for ease
    objects = ''
    for child in root.iter('object'):
        bndbox = child.find('bndbox')
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text
        objects += str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + ',classtobeadded! '
    line = path + ' ' + objects + '\n'
    items.append(line)
    print(items)

write_lines = open(os.path.join(base_dir, 'train.txt'), 'w')
for i in range(len(items)):
    write_lines.write(items[i])

write_lines.close()


# xml = os.path.join(base_dir, 'A3400_NB1_RAV_R07_180516084515_frame_3984.xml')

# tree = ET.parse(xml)
# root = tree.getroot()

# root[0]

# path = root.find('path').text
# items = []
# objects = ''
# for child in root.iter('object'):
#     # print(child.find('name'), child.find('name').text)
#     bndbox = child.find('bndbox')
#     xmin = bndbox.find('xmin').text
#     ymin = bndbox.find('ymin').text
#     xmax = bndbox.find('xmax').text
#     ymax = bndbox.find('ymax').text
#     print(path, 'xmin', xmin, 'ymin', ymin, 'xmax', xmax, 'ymax', ymax, 'class yet to be added!')
#     objects += str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + ',classtobeadded!'
# line = path + objects + '\n'
# items.append(line)
# print(objects)
# print(items)
