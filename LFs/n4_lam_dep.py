from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_4(x):
    try:
        keyword = ['tóc', 'da', 'môi', 'mũi', 'mụn', 'tai']
        if x['check_btype'] == 'Dịch vụ chăm sóc sức khỏe, sắc đẹp':
            for i in keyword:
                if i in x['name_cleaned']:
                    return 4
        elif x['check_btype'] != 'Dịch vụ chăm sóc sức khỏe, sắc đẹp':
            pass
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_4]

def get_lfs():
    return lfs