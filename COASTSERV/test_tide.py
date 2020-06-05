from coastserv.models.tide import Tide
import os

coords = [-16, 16, 40, 80]

path_in = os.path.join('/app', 'data', 'in')

options_path = os.path.join(path_in, 'options_tide.txt')


with open(options_path) as f:
    lines = f.readlines()
    for line in lines:
        li = line.strip()
        if not li.startswith("#"):
            print(li)
            if li.startswith('FESpath'):
                fesval = li.strip().split('=')[-1].strip()
            if li.startswith('coords'):
                coordsline = li.strip().split('=')[-1].strip()
                coordsval = [float(c) for c in coordsline.strip().split(',')]
            if li.startswith('pli'):
                plival = li.strip().split('=')[-1].strip()




path = os.path.abspath(os.path.join('/app', 'data', 'in', fesval))
pli = os.path.join('/app', 'data', 'in', plival)
out = os.path.join('/app', 'data', 'out')
if not os.path.exists(out):
    os.makedirs(out)
test = Tide(path, coordsval, pli, out)
test.build_tide()
