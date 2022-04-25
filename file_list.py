#%%
import  os

list_file = "ok_list.txt"
path = './ok/'

all_str = ''
files = os.listdir(path)

for file in files:
  str = path + file
  all_str = all_str + str + '\n'

with open(list_file, mode='w', encoding='utf-8')as f:
  f.write(all_str)
# %%
