## tf 22/08/18
## Read in the pascal voc file and produce a file that 
import os
import xml.etree.ElementTree as ET

base_dir = '/Users/datascience4/Documents/training3'
print(len(os.listdir(base_dir)))
xml_files = os.listdir(base_dir)
xml_files = [x for x in os.listdir(base_dir) if '.xml' in x]
print(xml_files)
items = []

##also create add a classes.txt file, which takes the object name and pushes it out
## create a file that creates a  tuple to enumerate the list
classes = []
count_classes = {}

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
    object_xml = ''
    for child in root.iter('object'):
        name = child.find('name').text
        ## write classes out to a file as well
        ## needed for yolo
        if not name in classes:
            classes += [name]
            count_classes[name] = 0
        class_pos = classes.index(name)
        count_classes[name] += 1
        print(classes)
        print(count_classes)
        if child.find('bndbox'):
            bndbox = child.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
            # instead of instruction to write multiple objects on one line,
            # as per original documentation separate out into one object per
            # line.
            object_xml = str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' \
                + str(ymax) + ',' + str(class_pos)
            if bool(object_xml) == True:
                line = path + ' ' + object_xml + '\n'
                items.append(line)

print(classes)
print(count_classes)

write_lines = open(os.path.join(base_dir, 'train.txt'), 'w')
for i in range(len(items)):
    write_lines.write(items[i])
write_lines.close()

write_classes = open(os.path.join(base_dir, 'classes.txt'), 'w')
for i in range(len(classes)):
    write_classes.write(classes[i] + '\n')
write_classes.close()

write_count_classes = open(os.path.join(base_dir, 'count_classes.txt'), 'w')
for key, value in count_classes.items():
    write_count_classes.write(key + ': ' + str(value) + '\n')
write_count_classes.close()