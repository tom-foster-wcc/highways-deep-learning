# Create the object for this
import os
import pandas as pd

print(os.listdir('../SCANNER 2018 VIDEO/70093 WARWICKSHIRE'))

# Create a file so that it takes each GPS location from each lup file and
# associates the file location with co-ordinates
# Additionally the object would also need extending at a later date.

# For now use the frames folder data set

print(os.listdir('../frames/data'))

all_files = os.listdir('../SCANNER 2018 VIDEO/70093 WARWICKSHIRE')
FRAMES_FOLDER = os.listdir('../frames/data')

lup_files = [x for x in all_files if '.lup' in x]
lup_files.sort()

lup_less_files = list(lup_files)
for x in range(len(lup_less_files)):
    lup_less_files[x] = lup_less_files[x][0:-4]
    x += 1
lup_less_files.sort()

# the A38 northbound
print(lup_less_files[2])
a38 = lup_less_files[2]

if a38 in lup_less_files:
    # need to improve the writign  of this.
    # Need to do this so it takes into account all files now once they are produced.
    read_file = pd.read_table('../SCANNER 2018 VIDEO/70093 WARWICKSHIRE/' + lup_files[2],
        header=None,
        delimiter=',',
        names=['FrameID', 'Lat', 'North', 'Long', 'West'])
    
    all_frame_objects = {}
    for row in read_file.FrameID:
        print(a38 + '_frame_' + str(row) + '.jpg')
        print(read_file.Lat[(row-1)])
        # Lat and long figures have rounding issues that do not show up in the
        # actual file
        all_frame_objects[a38 + '_frame_' + str(row) + '.jpg'] = {
            'lat' : read_file.Lat[(row-1)],
            'long' : read_file.Long[(row-1)],
            'labels' : [],
        }
    print(read_file.head())
    print(read_file.tail())
    print(read_file.Lat.head())
    print(read_file.Lat[0])
    print('worked?')

    

print(read_file.columns)
# Also will need to do it so that the frame location is correct.
print(lup_less_files[2])
print(read_file.iloc[2,:])
print(all_frame_objects)
print(list(all_frame_objects.keys())[-1])
print(read_file.tail())