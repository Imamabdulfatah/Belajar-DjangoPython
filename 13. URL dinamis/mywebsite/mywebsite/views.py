from django.http import HttpResponse

def link (request,page):
    str = "<h1>{}<?h1>".format(page)
    return HttpResponse(str)

def index(request):
    return HttpResponse("<h1>HOME</h1>")

def angka(request,input):
    heading = "<h1> Page Angka </h1>"
    str = heading + input
    return HttpResponse(str)

def tanggal(request,**input):
    print(input)
    tahun = input['tahun']
    bulan = input['bulan']
    hari = input['hari']
    heading = "<h1> Page tanggal </h1>"
    dataTanggal = "{}/{}/{}".format(tahun,bulan,hari)

    return HttpResponse(heading + dataTanggal)

# def tanggal(request,tahun,bulan):
#     heading = "<h1> Page Tanggal </h1>"
#     strTahun = "tahun: " + tahun
#     strBulan = "bulan: " + bulan
#     strTahun = heading + strTahun + "<br>" + strBulan + "br" + strHari
#     return HttpResponse(str)