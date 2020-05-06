from django.shortcuts import render
from .models import Product
from .appfunc.checker import barcoshifter
# Create your views here.


def binchecker(req):
    if req.method == 'POST':
        if '\r\n' in req.POST.get('body'):
            texts = ''
            for i in req.POST.get('body').split('\r\n'):
                if i != '':
                    texts += '<tr>'+result(i)+'</tr>'
        else:
            texts = '<tr>'+result(req.POST.get('body'))+'</tr>'
    dict1 = {
        'result': r'结果：',
        'html_content': '<br/><table>'+texts+'</table>',
    }
    return render(req, 'checkform.html', dict1)


def result(barcodes):
    barcode = barcoshifter(barcodes)
    if 'lop1_avg' in barcode.keys():
        lopavg = barcode.pop('lop1_avg')
    wd = Product.objects.filter(**barcode)
    if wd.exists():
        res = 'True'
        color = 'green'
        if wd.count() != 1:
            wd.filter(lop1_avgmin__lt=lopavg, lop1_avgmax__gte=lopavg)
            res += wd.count()
            color = 'yellow'
    else:
        res = 'False'
        color = 'red'
    wd = ' '.join([barcode['exproduct_name'],
                   barcode['spec_name'],
                   barcode['bin_no'],
                   barcodes.split(',')[16],
                   ])
    text = '<td>' + str(wd) + '</td>' + '<td><span style=color:' + color + '>' + res + '</span></td>'
    return text


def binform(req):
    dict1 = {
        'result': r'下方输入片号，回车换行',

    }
    return render(req, 'checkform.html', dict1)

