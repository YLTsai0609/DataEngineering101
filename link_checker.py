import os

all_mds = [file for file in os.listdir('.')
           if file.endswith('md') 
           and file != 'README.md'] 
paper_tag = 'Paper'
read_paper_counts = 0
# _io.TextIOWrapper, readline as a method to give line, generator backend
readme_file_obj = open('README.md') 
line = readme_file_obj.readline()
print(f'all record of markdown {len(all_mds)}')
print('checking all the markdown is in README.md or not...')
while line:
    if line:
        for md in all_mds:
            if md in line:
                all_mds.remove(md)
        if paper_tag in line:
            read_paper_counts += 1
    line = readme_file_obj.readline()

if all_mds:
    print(f'there are no record on README.md but exist {all_mds}')
else:
    print('-'*60)
    print('Done!')
    print(f'You have read {read_paper_counts} papers abstrsct, keep researching!')
    print('all clear, commit the repo =)')