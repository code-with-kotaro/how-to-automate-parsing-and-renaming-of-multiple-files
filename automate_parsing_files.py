import os

os.chdir('C:\\Users\\hussain akbar\\Desktop\\Oriental Restaurant\\Top 11 Best Selling')

# print(os.getcwd())

nums = 1
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    l_name = f_name.split(',')
    l_name.insert(0, str(nums).zfill(2))
    nums += 1
    full_name = ' '.join(l_name)
    # print(f'{full_name}{f_ext}')
    new_full_name = f'{full_name}{f_ext}'

    os.rename(f, new_full_name)