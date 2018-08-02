import os

print(os.listdir('../SCANNER 2018 VIDEO/70093 WARWICKSHIRE'))

all_files = os.listdir('../SCANNER 2018 VIDEO/70093 WARWICKSHIRE')

print(all_files)

video_only = [x for x in all_files if '.avi' in x]
syn_files = [x for x in all_files if '.syn' in x]
lup_files = [x for x in all_files if '.lup' in x]
tim_files = [x for x in all_files if '.tim' in x]
txt_files = [x for x in all_files if '.txt' in x]

print('all files length: ' + str(len(all_files)))
print('video_only: ' + str(len(video_only)))
print('syn files:' + str(len(syn_files)))
print('lup files:' + str(len(lup_files)))
print('tim files:' + str(len(tim_files)))
print('txt files:' + str(len(txt_files)))

for v in range(len(video_only)):
    print(video_only[v])
    v += 1

lup_less_files = list(lup_files)
for x in range(len(lup_less_files)):
    lup_less_files[x] = lup_less_files[x][0:-4]
    x += 1
lup_less_files.sort()

avi_less_files = list(video_only)
for x in range(len(avi_less_files)):
    avi_less_files[x] = avi_less_files[x][0:-4]
    x += 1
avi_less_files.sort()

matching_files = 0
for x in range(len(lup_less_files)):
    if lup_less_files[x] in avi_less_files:
        matching_files += 1
    else:
        print('not matching')
print(avi_less_files[0], lup_less_files[0])
print('matching files: ' + str(matching_files))