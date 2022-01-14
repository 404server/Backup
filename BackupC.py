import os
import time

source=[str(input('Enter path  from '))]
target_dir=str(input('Enter second  path to '))
if os.path.exists(target_dir):
     target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
     zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
     if os.system(zip_command)==0:
         print('Created')
     else:
         print('Not created')
else:
    print('Wrong way try again')
