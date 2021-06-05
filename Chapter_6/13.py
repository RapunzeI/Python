agencies = {'CCC':'Civilian Conservation Corps', 'FCC':'Federal Communications Commission', 'FDIC':'Federal Deposit Insurance Corporation',
            'SSB':'Social Security Board', 'WPA':'Works Progress Administration'}
            
agencies['SEC'] = 'Securities and Exchange Commission'
agencies['SSB'] = 'Social Security Administration'
agencies.pop('CCC' and 'WPA')

print(agencies.keys())