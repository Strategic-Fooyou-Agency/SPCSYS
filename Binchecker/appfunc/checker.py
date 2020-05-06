wd = r'S-06R1SUA-A,19B260213TWF00236,620EL1U,68409,VF:2.20,2.21,2.29,0.01,IV:300.0,313.2,330.0,8.88,WD:620.2,621.1,622.0,0.37,00-0A-0B-000-E40-Z,2019-12-17'
wd1 = r'S-09R1MUX-A,19C260046T6O00338,620EM1U,55755,VF:2.11,2.13,2.22,0.02,IV:360.1,382.9,390.0,5.54,WD:620.7,621.7,624.0,0.55,00-0A-00-00Y-E30-Z,2020-01-09'


def barcoshifter(wd):
    attr = wd.split(',')
    try:
        spec = attr[16].split('-')
    except IndexError:
        print(attr)
    attr_dict = {
        'exproduct_name': attr[0],
        'bin_no': attr[1][-4:-1],
        'spec_name': attr[2],
        'vf1_max': attr[6],
        'vf1_min': attr[4][3:],
        'wld1_max': attr[14],
        'wld1_min': attr[12][3:],
        'lop1_max': float(attr[10]),
        'lop1_min': float(attr[8][3:]),
        'vfspec': spec[0],
        'ivspec': spec[1],
        'wdspec': spec[2],
        'prod_no': spec[3],
        'process_code': spec[4],

    }
    # for i in attr:
    #     print(attr.index(i), i)
    if not produshifter(attr[0]):
        return attr_dict
    else:
        attr_dict['lop1_avg'] = attr[9]
        return attr_dict


def produshifter(name):
    names = ('S-06R1SUA', 'S-07R1SUA')
    for i in names:
        if name[:7] in i:
            return 1
    return 0
print(barcoshifter(wd))