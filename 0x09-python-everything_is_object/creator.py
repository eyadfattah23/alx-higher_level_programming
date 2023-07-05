import os

f_name = 'Tasks'
if not os.path.exists(f_name):
    os.makedirs(f_name)
    
for i in range(29):
    fil = f"{i}-answer.txt"
    with open(fil, 'w') as f:
        f.write('\n')
