from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import mysql
from mysql.connector import Error
from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import logging, traceback
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt
from Registration_Cust import config
from Registration_Cust import constants

def Registration(request):
    return render(request, 'HoardingBooker/Registration_Cust.html')


def Registration1(request):
    return render(request, 'HoardingBooker/Registration_PH.html')


def Registration2(request):
    return render(request, 'HoardingBooker/Registration_Pc.html')


def insertvalue(request):
    try:
        cname = request.GET.get('uname')
        ccity = request.GET.get('cname')
        cmob = int(request.GET.get('mob'))
        cemail = request.GET.get('email')

        conn = mysql.connector.connect(host='localhost', database='myproject', user='root', password='root')
        cursor = conn.cursor()
        query = "insert into custreg(cname,ccity,cmob,cemail) VALUES('%s','%s','%d','%s') " % (
            cname, ccity, cmob, cemail )
        cursor.execute(query)

        conn.commit()
        return HttpResponse('successfully inserted values')

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def insertvalue1(request):
    try:
        phname = request.GET.get('phname')
        phaddress = request.GET.get('phaddress')
        phmob = int(request.GET.get('phmob'))
        phcity = request.GET.get('phcity')
        document = request.GET.get('document')

        conn = mysql.connector.connect(host='localhost', database='myproject', user='root', password='root')
        cursor = conn.cursor()
        query1 = "insert into phreg(phname,phaddress,phmob,phcity,document) VALUES('%s','%s','%d','%s','%s') " % (
            phname, phaddress, phmob, phcity, document )
        cursor.execute(query1)

        conn.commit()
        return HttpResponse('successfully inserted values')

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def insertvalue2(request):
    try:
        pcname = request.GET.get('pcname')
        pcaddress = request.GET.get('pcaddress')
        pcmob = int(request.GET.get('pcmob'))
        pcemail = request.GET.get('email')
        document = request.GET.get('document')

        conn = mysql.connector.connect(host='localhost', database='myproject', user='root', password='root')
        cursor = conn.cursor()
        query2 = "insert into pcreg(pcname,pcaddress,pcmob,pcemail,document) VALUES('%s','%s','%s','%s','%s') " % (
            pcname, pcaddress, pcmob, pcemail, document )
        cursor.execute(query2)

        conn.commit()
        return HttpResponse('successfully inserted values')

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def categorywiseplace(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()

    q = "SELECT * FROM category"
    cursor.execute(q)
    row = cursor.fetchall()

    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()

    cid = int(request.GET.get('id'))
    name = request.GET.get('name')
    query = "SELECT * FROM placedetails WHERE cid='%d'" % ((cid))
    cursor.execute(query)
    rows2 = cursor.fetchall()
    print('rows', rows2)

    return render(request, 'HoardingBooker/categorywiseplace.html',
                  {'row': row, 'rows1': rows1, 'rows2': rows2, 'name': name})


def categorywisedesign(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()

    q = "SELECT * FROM category"
    cursor.execute(q)
    row = cursor.fetchall()

    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()

    id = request.session.get('lid')
    cid = int(request.GET.get('id'))
    name = request.GET.get('name')
    query = "SELECT * FROM designdetails WHERE dcatid='%d'" % ((cid))
    cursor.execute(query)
    rows2 = cursor.fetchall()
    print('rows', rows2)

    return render(request, 'HoardingBooker/categorywisedesign.html',
                  {'row': row, 'rows1': rows1, 'rows2': rows2, 'name': name })


def index(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    return render(request, 'HoardingBooker/index.html', {'rows': rows, 'rows1': rows1})


def adminindex(request):
    return render(request, 'HoardingBooker/adminindex.html')


def Registration_PH(request):
    return render(request, 'HoardingBooker/Registration_PH.html')


def Registration_Pc(request):
    return render(request, 'HoardingBooker/Registration_Pc.html')


def Registration_Cust(request):
    return render(request, 'HoardingBooker/Registration_Cust.html')


def login(request):
    return render(request, 'HoardingBooker/login.html')


def header(request):
    return render(request, 'HoardingBooker/header.html')


def header2(request):
    return render(request, 'HoardingBooker/header2.html')


def footer(request):
    return render(request, 'HoardingBooker/footer.html')


def pcindex(request):
    return render(request, 'HoardingBooker/pcindex.html')


def phindex(request):
    return render(request, 'HoardingBooker/phindex.html')


def contact(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    return render(request, 'HoardingBooker/contact.html', {'rows1': rows1, 'rows': rows})


def pcadddetails(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows = cursor.fetchall()
    return render(request, 'HoardingBooker/pcadddetails.html', {'cat': rows})


def phadddetails(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    print("category", rows)
    return render(request, 'HoardingBooker/phadddetails.html', {'cat': rows})


def designcompany(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    return render(request, 'HoardingBooker/designcompany.html', {'rows': rows, 'rows1': rows1})


def customizeform(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    return render(request, 'HoardingBooker/customizeform.html', {'rows': rows, 'rows1': rows1})


def viewrequest(request):
    return render(request, 'HoardingBooker/viewrequest.html')


def custindex(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()



    return render(request, 'HoardingBooker/custindex.html', {'rows': rows, 'rows1': rows1})


def addcategory(request):
    return render(request, 'HoardingBooker/addcategory.html')


def pcaddcategory(request):
    return render(request, 'HoardingBooker/pcaddcategory.html')


def phreg(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST' and request.FILES['phdoc']:
            phname = request.POST.get('phname')
            phcname = request.POST.get('phcname')
            phadd = request.POST.get('phadd')
            phmob = int(request.POST.get('phmob'))
            phemail = request.POST.get('phemail')
            phdoc = request.FILES['phdoc']
            phcrpwd = request.POST.get('phcrpwd')
            fs = FileSystemStorage()
            filename = phdoc.name
            extension = filename.split('.')
            uploaded_file_name = phcname + "." + extension[1]
            filename = fs.save(uploaded_file_name, phdoc)
            uploaded_file_url = fs.url(filename)

            # for insert data in logintable
            query = " INSERT INTO login (lcat,uname , pwd) VALUES('%s', '%s','%s') " % ( 'Placeholder', phname, phcrpwd)
            cursor.execute(query)
            conn.commit()

            lid = cursor.lastrowid
            print("lastworid", lid)

            # for insert data in register table with foreign key lid
            qry = "INSERT INTO phreg (phname,phcname, phadd,phmob,phemail,phdoc, lid,status) VALUES ('%s','%s','%s','%d','%s','%s','%d','%s') " \
                  % (phname, phcname, phadd, phmob, phemail, uploaded_file_url, lid, 'Pending')
            cursor.execute(qry)
            conn.commit()

            return render(request, "hoardingbooker/login.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def pcreg(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST' and request.FILES['pcclogo']:
            pcname = request.POST.get('pcname')
            pccname = request.POST.get('pccname')
            myfile = request.FILES['pcclogo']

            print('logo', myfile)
            pcadd = request.POST.get('pcaddress')
            pcmob = int(request.POST.get('pcmob'))
            pcemail = request.POST.get('pcemail')
            pcdoc = request.FILES['pcdoc']
            print('doc', pcdoc)
            pccrpwd = request.POST.get('pccrpwd')

            fs = FileSystemStorage()
            filename = myfile.name
            extension = filename.split('.')
            uploaded_file_name = pccname + "." + extension[1]
            # filename = fs.save(uploaded_file_name, myfile)
            # uploaded_file_url = fs.url(filename)
            # print('upload file url', uploaded_file_url)

            fs1 = FileSystemStorage()
            docname = pcdoc.name
            print('docname', docname)
            ext = docname.split('.')
            upload_doc_name = pccname + "." + ext[1]
            print('upload doc name', upload_doc_name)
            # docname = fs1.save(upload_doc_name, docname)
            # upload_doc_url = fs1.url(docname)
            # print('upload doc url', upload_doc_url)
            # for insert data in logintable
            query = " INSERT INTO login (lcat,uname , pwd) VALUES('%s', '%s','%s') " % (
                'Paintingcompany', pcname, pccrpwd)
            cursor.execute(query)
            conn.commit()

            lid = cursor.lastrowid
            print("lastworid", lid)

            # for insert data in register table with foreign key lid
            qry = "INSERT INTO pcreg (pcname,pccname, pcadd,pcmob,pcemail,pcdoc, loginid,status,pcclogo) VALUES ('%s','%s','%s','%d','%s','%s','%d','%s','%s') " \
                  % (pcname, pccname, pcadd, pcmob, pcemail, upload_doc_name, lid, 'pending', uploaded_file_name)
            cursor.execute(qry)
            conn.commit()

            return render(request, "hoardingbooker/login.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def custreg(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'GET':
            cname = request.GET.get('cname')
            cmob = int(request.GET.get('cmob'))
            cemail = request.GET.get('cemail')
            ccrpwd = request.GET.get('ccrpwd')
            cintrest = request.GET.get('intrest')
            caddress = request.GET.get('address')
            # for insert data in logintable
            query = " INSERT INTO login (lcat,uname , pwd) VALUES('%s', '%s','%s') " % ( 'Customer', cname, ccrpwd)
            cursor.execute(query)
            conn.commit()

            lid = cursor.lastrowid

            print("lastworid", lid)

            # for insert data in register table with foreign key lid
            qry = "INSERT INTO custreg (cname,cmob,cemail, loginid1,caddress, cintrest) VALUES ('%s','%d','%s','%d','%s','%s') " \
                  % (cname, cmob, cemail, lid , caddress,cintrest)
            cursor.execute(qry)
            conn.commit()

            return render(request, "hoardingbooker/login.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def Authenticate(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        if request.method == 'GET':
            username = request.GET.get('uname')
            password = request.GET.get('pwd')
            q = "SELECT lid,lcat FROM login WHERE uname = '%s' AND pwd = '%s'" % (username, password)
            cursor.execute(q)
            rows = cursor.fetchall()
            print('rows', rows)
            if not rows:
                msg = "Please Enter correct username  password..!"
                return render(request, 'hoardingbooker/login.html', {'msg': msg})
            else:
                for row in rows:
                    print(row[0])
                    print('lcat : ', row[1])
                    cursor.execute(q)
                    rows = cursor.fetchall()
                    request.session['lid'] = row[0]

                if row[1] == 'Placeholder':
                    qr = "SELECT status FROM phreg WHERE lid = '%d'" % (row[0])
                    cursor.execute(qr)
                    status = cursor.fetchone()
                    print('status', status[0])
                    if (status[0] == 'Accepted'):
                        return render(request, 'hoardingbooker/phindex.html', {'lid': row[0]})
                    else:
                        msg = 'Please wait for admin approval.'
                        return render(request, 'hoardingbooker/login.html', {'msg': msg})

                elif row[1] == 'Paintingcompany':
                    qr = "SELECT status FROM pcreg WHERE loginid = '%d'" % (row[0])
                    cursor.execute(qr)
                    status = cursor.fetchone()
                    print('status', status[0])
                    if (status[0] == 'Accepted'):
                        return render(request, 'hoardingbooker/pcindex.html', {'lid': row[0]})
                    else:
                        msg = 'Please wait for admin approval.'
                        return render(request, 'hoardingbooker/login.html', {'msg': msg})
                elif row[1] == 'Customer':
                    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root',
                                                   password='root')
                    cursor = conn.cursor()
                    q = "SELECT * FROM category"
                    cursor.execute(q)
                    rows = cursor.fetchall()
                    q = "SELECT * FROM category1"
                    cursor.execute(q)
                    rows1 = cursor.fetchall()



                    id = request.session.get('lid')

                    q = "select cintrest from custreg WHERE loginid1='%d'" % (id)
                    cursor.execute(q)
                    type = cursor.fetchone()
                    print(type)
                    q1 = "SELECT * FROM designdetails  where designdetails.dtype= '%s'" % (type)
                    cursor.execute(q1)
                    rows2 = cursor.fetchall()


                    return render(request, 'hoardingbooker/custindex.html',
                                  {'lid': row[0], 'rows': rows, 'rows1': rows1,'data':rows2})
                elif row[1] == 'admin':
                    return render(request, 'hoardingbooker/adminindex.html', {'lid': row[0]})

        else:
            return render(request, 'hoardingbooker/login.html')
            conn.commit()

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def pcadddetailsinsert(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST' and request.FILES['pcpic']:
            myfile = request.FILES['pcpic']
            dname = request.POST.get('dname')
            dcatid = int(request.POST.get('cat'))
            dsize = request.POST.get('dsize')
            dtype = request.POST.get('dtype')
            dmaterial = request.POST.get('dmaterial')
            dprice = request.POST.get('dprice')
            lid = request.session.get('lid')
            ddiscript = request.POST.get('ddiscript')
            print('lid', lid)
            fs = FileSystemStorage()
            filename = myfile.name
            extension = filename.split('.')
            uploaded_file_name = dname + "." + extension[1]
            filename = fs.save(uploaded_file_name, myfile)
            print("uploaded_file_name", filename)
            uploaded_file_url = fs.url(filename)
            print("uploaded_file_url", uploaded_file_url)

        qry = "INSERT INTO designdetails (pcpic,dname,dsize,dtype,dmaterial,dprice,logid,ddiscript,dcatid) VALUES ('%s','%s','%s','%s','%s','%s','%d','%s','%d') " \
              % (uploaded_file_url, dname, dsize, dtype, dmaterial, dprice, lid, ddiscript, dcatid)
        cursor.execute(qry)
        conn.commit()
        msg = "succesfully added..!"
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows = cursor.fetchall()

        return render(request, "hoardingbooker/pcadddetails.html", {'msg': msg, 'cat': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def phadddetailsinsert(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST' and request.FILES['phpic']:
            myfile = request.FILES['phpic']
            catid = int(request.POST.get('cat'))
            pname = request.POST.get('pname')
            psize = request.POST.get('psize')
            parea = request.POST.get('parea')
            pprice = request.POST.get('pprice')
            lid = request.session.get('lid')
            pdiscript = request.POST.get('pdiscript')
            print('lid', lid)
            fs = FileSystemStorage()
            filename = myfile.name
            extension = filename.split('.')
            uploaded_file_name = pname + "." + extension[1]
            filename = fs.save(uploaded_file_name, myfile)
            print("uploaded_file_name", filename)
            uploaded_file_url = fs.url(filename)
            print("uploaded_file_url", uploaded_file_url)

        qry = "INSERT INTO placedetails (phpic,pname,psize,parea,pprice,logid2,pdiscript,cid) VALUES ('%s','%s','%s','%s','%s','%d','%s','%d') " \
              % (uploaded_file_url, pname, psize, parea, pprice, lid, pdiscript, catid)
        cursor.execute(qry)
        conn.commit()
        msg = "successfully added..!"
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        return render(request, "hoardingbooker/phadddetails.html", {'msg': msg, 'cat': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdata(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')

        query = "SELECT * FROM designdetails WHERE logid='%d'" % (int(lid))
        cursor.execute(query)
        rows = cursor.fetchall()
        print('rows', rows)

        return render(request, 'HoardingBooker/pcindex.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdataph(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')

        query = "SELECT * FROM placedetails WHERE logid2='%d'" % (int(lid))
        cursor.execute(query)
        rows = cursor.fetchall()
        print('rows', rows)

        return render(request, 'HoardingBooker/phindex.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def verifypc(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        query = "SELECT * FROM pcreg where status='%s'" % ('pending')
        cursor.execute(query)
        rows = cursor.fetchall()

        return render(request, 'HoardingBooker/verifypc.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def acceptpc(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = request.GET.get('id')
        print('pcid', id)
        query = "Update pcreg SET status='%s' WHERE (pcid='%d')" % ("Accepted", int(id))
        cursor.execute(query)
        conn.commit()
        print(query)
        return verifypc(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def rejectpc(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = request.GET.get('id')
        print('pcid', id)
        query = "Update pcreg SET status='%s' WHERE (pcid='%d')" % ("Rejected", int(id))
        cursor.execute(query)
        conn.commit()
        print(query)
        return verifypc(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def verifyph(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        query = "SELECT * FROM phreg where status='%s'" % ('pending')
        cursor.execute(query)
        rows = cursor.fetchall()

        return render(request, 'HoardingBooker/verifyph.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def acceptph(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = request.GET.get('id')
        print('phid', id)
        query = "Update phreg SET status='%s' WHERE (phid='%d')" % ("Accepted", int(id))
        cursor.execute(query)
        conn.commit()
        print(query)
        return verifyph(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def rejectph(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = request.GET.get('id')
        print('phid', id)
        query = "Update phreg SET status='%s' WHERE (phid='%d')" % ("Rejected", int(id))
        cursor.execute(query)
        conn.commit()
        print(query)
        return verifyph(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdatadesign(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')

        query = "SELECT * FROM designdetails WHERE logid='%d'" % (int(lid))
        cursor.execute(query)
        rows = cursor.fetchall()
        print('rows', rows)

        return render(request, 'HoardingBooker/viewdesign.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def pcfetchdata(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = int(request.GET.get('id'))
        print(id)
        query = "select * from designdetails WHERE ddid ='%d'" % (id)
        cursor.execute(query)
        print(query)
        row = cursor.fetchone()
        print(row)
        catid = row[9]
        arrdata = []
        while row is not None:
            arrdata.append(row)
            row = cursor.fetchone()

        q = "SELECT * FROM category1 WHERE catid1='%d'" % (catid)
        cursor.execute(q)
        row = cursor.fetchall()

        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows = cursor.fetchall()

        return render(request, 'HoardingBooker/pcupdatedetails.html', {'data': arrdata, 'rows': rows, 'row': row})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def pcdetailsupdate(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST':
            id = int(request.POST.get('id'))
            myfile = request.FILES['pcpic']
            print(myfile)
            dname = request.POST.get('dname')
            catid = int(request.POST.get('cat'))
            print("catid", catid)
            dsize = request.POST.get('dsize')
            dtype = request.POST.get('dtype')
            dmaterial = request.POST.get('dmaterial')
            dprice = request.POST.get('dprice')

            ddiscript = request.POST.get('ddiscript')

            fs = FileSystemStorage()
            filename = myfile.name
            extension = filename.split('.')
            uploaded_file_name = dname + "." + extension[1]
            filename = fs.save(uploaded_file_name, myfile)
            print("uploaded_file_name", filename)
            uploaded_file_url = fs.url(filename)
            print("uploaded_file_url", uploaded_file_url)

            conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
            cursor = conn.cursor()

            query = "UPDATE designdetails SET pcpic='%s' , dname ='%s' , dsize ='%s' , dtype ='%s' , dmaterial ='%s' , dprice ='%s' , ddiscript = '%s' , dcatid = '%d' WHERE ddid='%d'" % (
                uploaded_file_url, dname, dsize, dtype, dmaterial, dprice, ddiscript, catid, id)
            cursor.execute(query)
            print(query)
            conn.commit()

            return viewdatadesign(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdataplace(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')

        query = "SELECT * FROM placedetails WHERE logid2='%d'" % (int(lid))
        cursor.execute(query)
        rows = cursor.fetchall()
        print('rows', rows)

        return render(request, 'HoardingBooker/viewplace.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def phfetchdata(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = int(request.GET.get('id'))
        print(id)
        query = "select * from placedetails WHERE pdid ='%d'" % (id)
        cursor.execute(query)
        print(query)
        row = cursor.fetchone()
        catid = row[8]
        arrdata = []
        while row is not None:
            arrdata.append(row)
            row = cursor.fetchone()

        q = "SELECT * FROM category WHERE catid='%d'" % (catid)
        cursor.execute(q)
        row = cursor.fetchall()

        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()

        return render(request, 'HoardingBooker/phupdatedetails.html', {'data': arrdata, 'rows': rows, 'row': row})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def phdetailsupdate(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST':
            id = int(request.POST.get('id'))
            myfile = request.FILES['phpic']
            pname = request.POST.get('pname')
            catid = int(request.POST.get('cat'))
            print("catid", catid)
            psize = request.POST.get('psize')
            parea = request.POST.get('parea')
            pprice = request.POST.get('pprice')
            lid = request.session.get('lid')
            pdiscript = request.POST.get('pdiscript')

            fs = FileSystemStorage()
            filename = myfile.name
            extension = filename.split('.')
            uploaded_file_name = pname + "." + extension[1]
            filename = fs.save(uploaded_file_name, myfile)
            print("uploaded_file_name", filename)
            uploaded_file_url = fs.url(filename)
            print("uploaded_file_url", uploaded_file_url)

            conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
            cursor = conn.cursor()
            query = "UPDATE placedetails SET phpic='%s' , pname ='%s' , psize ='%s' , parea ='%s'  , pprice ='%s' , pdiscript = '%s' ,cid ='%d'WHERE pdid='%d'" % (
                uploaded_file_url, pname, psize, parea, pprice, pdiscript, catid, id)
            cursor.execute(query)
            print(query)
            conn.commit()
            return viewdataplace(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def contactusdetails(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST':
            cuname = request.POST.get('Name')
            cuemail = request.POST.get('Email')
            cumob = int(request.POST.get('Telephone'))
            cusub = request.POST.get('Subject')
            cumsg = request.POST.get('Message')
            # for insert data in logintable
            query = " INSERT INTO contactusdetails (cuname , cuemail , cumob , cusub , cumsg) VALUES('%s', '%s','%s','%s','%s') " % (
                cuname, cuemail, cumob, cusub, cumsg)
            cursor.execute(query)
            print(query)
            conn.commit()

            return render(request, "hoardingbooker/contact.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdeletedesign(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')

        query = "SELECT * FROM designdetails WHERE logid='%d'" % (int(lid))
        cursor.execute(query)
        content = cursor.fetchall()
        print('rows', content)
        return render(request, 'HoardingBooker/deletedesign.html', {'content': content})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def pcdeletedesign(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = int(request.GET.get('id'))
        lid = request.session.get('lid')
        print(id)
        q = "SELECT daddtocart.dddetailsid , designdetails.ddid FROM daddtocart join designdetails on daddtocart.dddetailsid = designdetails.ddid WHERE designdetails.ddid='%d'" % (
            id)
        cursor.execute(q)
        rows = cursor.fetchone()
        print("rows", rows)
        q1 = "SELECT favouritedesign.did , designdetails.ddid FROM favouritedesign join designdetails on favouritedesign.did = designdetails.ddid WHERE designdetails.ddid='%d'" % (
            id)
        cursor.execute(q1)
        rows1 = cursor.fetchone()
        print("rows1", rows1)
        qry = "SELECT * FROM designdetails where logid = '%d'" % (int(lid))
        cursor.execute(qry)
        content = cursor.fetchall()
        if (rows != None or rows1 != None):  # if(rows[0]==id):
            lid = request.session.get('lid')
            query = "SELECT * FROM designdetails WHERE logid='%d'" % (int(lid))
            cursor.execute(query)
            rows = cursor.fetchall()

            print('rows', rows)
            msg = 'you can not delete this design because it is used by customer !!!'
            return render(request, 'HoardingBooker/deletedesign.html', {'content': content, 'msg': msg})
        else:
            query = "delete from designdetails WHERE ddid='%d'" % (id)
            cursor.execute(query)
            print(query)
            conn.commit()
            return viewdeletedesign(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdeleteplace(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')

        query = "SELECT * FROM placedetails WHERE logid2='%d'" % (int(lid))
        cursor.execute(query)
        rows = cursor.fetchall()
        print('rows', rows)

        return render(request, 'HoardingBooker/deleteplace.html', {'content': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def phdeleteplace(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        lid = request.session.get('lid')
        id = int(request.GET.get('id'))
        print(id)
        q = "SELECT paddtocart.pdetailsid , placedetails.pdid FROM paddtocart join placedetails on paddtocart.pdetailsid = placedetails.pdid WHERE placedetails.pdid='%d'" % (
            id)
        cursor.execute(q)
        rows = cursor.fetchone()
        print("rows", rows)
        q1 = "SELECT favouriteplace.pid , placedetails.pdid FROM favouriteplace join placedetails on favouriteplace.pid = placedetails.pdid WHERE placedetails.pdid='%d'" % (
            id)
        cursor.execute(q1)
        rows1 = cursor.fetchone()
        print("rows1", rows1)
        qry = "SELECT * FROM placedetails where logid2 = '%d'" % (int(lid))
        cursor.execute(qry)
        content = cursor.fetchall()

        if (rows != None or rows1 != None):  # if(rows[0]==id):
            lid = request.session.get('lid')
            query = "SELECT * FROM placedetails WHERE logid2='%d'" % (int(lid))
            cursor.execute(query)
            rows = cursor.fetchall()
            print('rows', rows)
            msg = 'you can not delete this design because it is used by customer !!!'
            return render(request, 'HoardingBooker/deleteplace.html', {'msg': msg, 'content': content})
        else:
            query = "delete from placedetails WHERE pdid='%d'" % (id)
            cursor.execute(query)
            print(query)
            conn.commit()
            return viewdeleteplace(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def customizeformdata(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST':
            custname = request.POST.get('custname')
            custmaterial = request.POST.get('custmaterial')
            custdsize = int(request.POST.get('custdsize'))
            custdtype = request.POST.get('custdtype')
            custbudget = request.POST.get('custbudget')
            custdname = request.POST.get('custdname')
            custreq = request.POST.get('custreq')
            compid = int(request.POST.get('compid'))
            custmid = int(request.POST.get('custmid'))
            # for insert data in logintable
            query = " INSERT INTO customizeform (custname , custmaterial , custbudget , custdname ,custdsize ,custdtype , custreq , paid , custmid , status) VALUES('%s', '%s','%s','%s','%s','%s','%s','%d','%d','%s') " % (
                custname, custmaterial, custbudget, custdname, custdsize, custdtype, custreq, compid, custmid,
                'pending')
            cursor.execute(query)
            print(query)
            conn.commit()
            return render(request, "hoardingbooker/customizeform.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewcompany(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        query = "SELECT * FROM pcreg "
        cursor.execute(query)
        data = cursor.fetchall()
        print('rows', rows)

        return render(request, 'HoardingBooker/designcompany.html', {'data': data, 'rows': rows, 'rows1': rows1})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def getcompid(request):
    compid = int(request.POST.get('compid'))
    custmid = request.session.get('lid')
    print('custid', custmid)
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    return render(request, "hoardingbooker/customizeform.html",
                  {'data': compid, 'data1': custmid, 'rows': rows, 'rows1': rows1})


def viewcustomizereq(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        query = "SELECT * FROM customizeform where status='%s'" % ('Pending')
        cursor.execute(query)
        rows = cursor.fetchall()

        return render(request, 'HoardingBooker/viewrequest.html', {'data': rows})

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def acceptform(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = request.GET.get('id')
        print('cfid', id)
        query = "Update customizeform SET status='%s' WHERE (cfid='%d')" % ("Accepted", int(id))
        cursor.execute(query)
        conn.commit()
        print(query)
        return viewcustomizereq(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def rejectform(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = request.GET.get('id')
        print('cfid', id)
        query = "Update customizeform SET status='%s' WHERE (cfid='%d')" % ("Rejected", int(id))
        cursor.execute(query)
        conn.commit()
        print(query)
        return viewcustomizereq(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def addcat(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST':
            catname = request.POST.get('catname')


            # for insert data in logintable
            query = " INSERT INTO category (catname) VALUES('%s') " % ( catname )
            cursor.execute(query)
            conn.commit()
            return render(request, "hoardingbooker/addcategory.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def pcaddcat(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        if request.method == 'POST':
            pccatname = request.POST.get('pccatname')


            # for insert data in logintable
            query = " INSERT INTO category1 (pccatname) VALUES('%s') " % ( pccatname )
            cursor.execute(query)
            conn.commit()
            return render(request, "hoardingbooker/pcaddcategory.html")

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def favouriteplace(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        row = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        pid = int(request.GET.get('pid'))
        print("place id", pid)
        lid = int(request.session.get('lid'))
        print("cust id", lid)

        q = "SELECT * FROM favouriteplace where pid='%d'and custid='%d'" % (pid, lid)
        cursor.execute(q)
        rows = cursor.fetchone()
        print("allready data", rows)
        if (rows == None):
            query = " INSERT INTO favouriteplace (custid,pid) VALUES('%d','%d') " % ((lid), int(pid))
            cursor.execute(query)
            conn.commit()
            msg = "successfully added"
        else:
            msg = "allready added"

        q = "SELECT * FROM favouriteplace where pid='%d'and custid='%d'" % (pid, lid)
        cursor.execute(q)
        rows = cursor.fetchall()
        print(rows)
        if (rows == None):
            return 0
        else:
            print("pid", rows[0][2])
            pid = rows[0][2]

        query = "select * from placedetails where cid= (SELECT cid FROM placedetails join category on placedetails.cid = category.catid  where placedetails.pdid = %d)" % (
            (pid))
        cursor.execute(query)
        rows2 = cursor.fetchall()
        print('rows', rows2)

        q1 = "SELECT cid FROM placedetails join category on placedetails.cid = category.catid  where placedetails.pdid = %d" % (
            pid)
        cursor.execute(q1)
        id = cursor.fetchone()
        print(id)
        q2 = "select catname from category WHERE catid=%d" % (id)
        cursor.execute(q2)
        name = cursor.fetchone()
        print(name[0])

        return render(request, 'HoardingBooker/categorywiseplace.html',
                      {'msg': msg, 'rows2': rows2, 'rows1': rows1, 'row': row, 'name': name[0]})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def favouritedesign(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        row = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        did = int(request.GET.get('did'))
        print("design id", did)
        lid = int(request.session.get('lid'))
        print("cust id", lid)

        q = "SELECT * FROM favouritedesign where did='%d'and custid='%d'" % (did, lid)
        cursor.execute(q)
        rows = cursor.fetchone()
        print("allready data", rows)
        if (rows == None):
            query = " INSERT INTO favouritedesign (custid,did) VALUES('%d','%d') " % ((lid), int(did))
            cursor.execute(query)
            conn.commit()
            msg = "successfully added"
        else:
            msg = "allready added"

        q = "SELECT * FROM favouritedesign where did='%d'and custid='%d'" % (did, lid)
        cursor.execute(q)
        rows = cursor.fetchall()
        print(rows)
        if (rows == None):
            return 0
        else:
            print("did", rows[0][2])
            did = rows[0][2]

        query = "select * from designdetails where dcatid= (SELECT dcatid FROM designdetails join category1 on designdetails.dcatid = category1.catid1  where designdetails.ddid = %d)" % (
            (did))
        cursor.execute(query)
        rows2 = cursor.fetchall()
        print('rows', rows2)

        q1 = "SELECT dcatid FROM designdetails join category1 on designdetails.dcatid = category1.catid1  where designdetails.ddid = %d" % (
            did)
        cursor.execute(q1)
        id = cursor.fetchone()
        print(id)
        q2 = "select pccatname from category1 WHERE catid1=%d" % (id)
        cursor.execute(q2)
        name = cursor.fetchone()
        print(name[0])

        return render(request, 'HoardingBooker/categorywisedesign.html',
                      {'msg': msg, 'rows2': rows2, 'rows1': rows1, 'row': row, 'name': name[0]})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewdfav(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    custid = request.session.get('lid')
    q = "SELECT * FROM favouritedesign RIGHT OUTER JOIN designdetails ON favouritedesign.did=designdetails.ddid where favouritedesign.custid=%d" % (
        custid)
    cursor.execute(q)
    rows2 = cursor.fetchall()
    print("category", rows)
    return render(request, 'HoardingBooker/viewdfav.html', {'rows2': rows2, 'rows': rows, 'rows1': rows1})


def viewpfav(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()
    custid = request.session.get('lid')
    q = "SELECT * FROM favouriteplace RIGHT OUTER JOIN placedetails ON favouriteplace.pid=placedetails.pdid where favouriteplace.custid=%d" % (
        custid)
    cursor.execute(q)
    rows2 = cursor.fetchall()
    print("category", rows)
    return render(request, 'HoardingBooker/viewpfav.html', {'rows': rows, 'rows1': rows1, 'rows2': rows2})


def viewddetails(request):
    try:

        id = int(request.GET.get('id'))
        print("did", id)
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()
        query = "SELECT * FROM designdetails where ddid='%d'" % (id)
        cursor.execute(query)
        rows2 = cursor.fetchall()
        return render(request, 'HoardingBooker/viewddetails.html', {'rows': rows, 'rows1': rows1, 'rows2': rows2})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewpdetails(request):
    try:

        id = int(request.GET.get('id'))
        print("pid", id)
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()
        query = "SELECT * FROM placedetails where pdid='%d'" % (id)
        cursor.execute(query)
        rows2 = cursor.fetchall()
        return render(request, 'HoardingBooker/viewpdetails.html', {'rows': rows, 'rows1': rows1, 'rows2': rows2})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def premovefav(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        fid = int(request.POST.get('fid'))
        print(fid)
        query = "delete from favouriteplace WHERE fid='%d'" % (fid)
        cursor.execute(query)
        print(query)
        conn.commit()
        return viewpfav(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def dremovefav(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        fid1 = int(request.POST.get('fid1'))
        print(fid1)
        query = "delete from favouritedesign WHERE fid1='%d'" % (fid1)
        cursor.execute(query)
        print(query)
        conn.commit()
        return viewdfav(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def daddtocart(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        did = int(request.GET.get('did'))
        print(did)
        query = "SELECT * FROM designdetails where ddid='%d' " % (did)
        cursor.execute(query)
        print(query)
        rows2 = cursor.fetchall()
        print(rows2)
        conn.commit()

        return render(request, 'HoardingBooker/daddtocart.html', {'rows': rows, 'rows1': rows1, 'rows2': rows2})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def daddtocart1(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        did = int(request.POST.get('id'))
        q = "SELECT dcatid FROM designdetails where ddid='%d' " % (did)
        cursor.execute(q)
        print(q)
        catid = cursor.fetchone()
        catid = catid[0]
        custid = request.session.get('lid')

        qty = int(request.POST.get('qty'))
        price = int(request.POST.get('totalp'))
        query = " INSERT INTO daddtocart (dddetailsid,ddcustid,ddcatid,ddtotalprice,ddqty) VALUES('%d','%d','%d','%d','%d') " % (
            did, custid, catid, price, qty)
        cursor.execute(query)
        print(query)
        conn.commit()
        return payment(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def paddtocart(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        pid = int(request.GET.get('pid'))
        print(pid)
        query = "SELECT * FROM placedetails where pdid='%d' " % (pid)
        cursor.execute(query)
        print(query)
        rows2 = cursor.fetchall()
        print(rows2)
        conn.commit()

        return render(request, 'HoardingBooker/paddtocart.html', {'rows': rows, 'rows1': rows1, 'rows2': rows2})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def paddtocart1(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        pid = int(request.POST.get('id'))
        q = "SELECT cid FROM placedetails where pdid='%d' " % (pid)
        cursor.execute(q)
        print(q)
        catid = cursor.fetchone()
        catid = catid[0]
        custid = request.session.get('lid')

        qty = int(request.POST.get('qty'))
        price = int(request.POST.get('totalp'))
        query = " INSERT INTO paddtocart (pdetailsid,pcustid,pcatid,pprice,pqty) VALUES('%d','%d','%d','%d','%d') " % (
            pid, custid, catid, price, qty)
        cursor.execute(query)
        print(query)
        conn.commit()
        return payment(request)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def payment(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        id = int(request.session.get('lid'))
        print(id)
        query = "SELECT * FROM paddtocart join placedetails on placedetails.pdid = paddtocart.pdetailsid WHERE paddtocart.pcustid = '%d' " % (
            id)
        cursor.execute(query)
        print(query)
        pdata = cursor.fetchall()
        print(pdata)
        query = "SELECT * FROM daddtocart join designdetails on designdetails.ddid = daddtocart.dddetailsid WHERE daddtocart.ddcustid = '%d' " % (
            id)
        cursor.execute(query)
        print(query)
        ddata = cursor.fetchall()
        print(ddata)

        query = "select sum(paddtocart.pprice) as ptotal from paddtocart where pcustid=%d" % (id)
        cursor.execute(query)
        ptotal = cursor.fetchone()
        print('ptotal', ptotal)
        query = "select sum(daddtocart.ddtotalprice) as dtotal from daddtocart where ddcustid=%d" % (id)
        cursor.execute(query)
        dtotal = cursor.fetchone()
        print('dtotal', dtotal)

        total = []
        total1 = ptotal + dtotal
        total.append(total1)

        results = [tuple(str(item) for item in t) for t in total]

        t = results[0]

        a = t[0]

        b = t[1]

        c = int(a) + int(b)
        print(c)
        request.session['cm'] = c

        id = request.session.get('lid')
        qry = "SELECT * FROM custreg where loginid1='%d' " % (id)
        cursor.execute(qry)
        print(qry)
        details = cursor.fetchone()
        print(details)

        uname = details[1]

        address = details[5]
        uemail = details[3]
        mob = details[2]
        request.session['name'] = uname
        request.session['email'] = uemail

        data = {'rows': rows, 'rows1': rows1, 'pdata': pdata, 'ddata': ddata, 'total': c }
        txnid = get_transaction_id()
        hash_ = generate_hash(request, txnid)
        hash_string = get_hash_string(request, txnid)
        # use constants file to store constant values.
        # use test URL for testing
        data["action"] = constants.PAYMENT_URL_LIVE
        data["amount"] = float(c)
        data["productinfo"] = constants.PAID_FEE_PRODUCT_INFO
        data["key"] = config.KEY
        data["txnid"] = txnid
        data["hash"] = hash_
        data["hash_string"] = hash_string
        data["firstname"] = uname
        data["email"] = uemail
        data["address"] = address
        data["phone"] = mob
        data["service_provider"] = constants.SERVICE_PROVIDER
        data["furl"] = request.build_absolute_uri(reverse("Registration_Cust:payment_failure"))
        data["surl"] = request.build_absolute_uri(reverse("Registration_Cust:payment_success"))



    # for row  in total:
    # total.append(list(map(str, list(row))))
    # print(total)

    # finaltotal = var_fixed[0] + var_fixed[1]
    # print("final",finaltotal)

        return render(request, 'HoardingBooker/payment.html',data)

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def generate_hash(request, txnid):
    try:
        # get keys and SALT from dashboard once account is created.
        # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string = get_hash_string(request, txnid)
        generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        # log the error here.
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


# create hash string using all the fields
def get_hash_string(request, txnid):
    hash_string = config.KEY + "|" + txnid + "|" + str(
        float(request.session.get('cm'))) + "|" + constants.PAID_FEE_PRODUCT_INFO + "|"
    # hash_string += request.session["student_user"]["name"] + "|" + request.session["student_user"]["email"] + "|"
    # hash_string += "||||||||||" + config.SALT
    hash_string += request.session.get('name') + "|" + request.session.get('email') + "|"
    hash_string += "||||||||||" + config.SALT

    return hash_string


# generate a random transaction Id.
def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0, 9999)).encode("utf-8"))
    # take approprite length
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid


# no csrf token require to go to Success page.
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
    data = {}
    return render(request, "HoardingBooker/success.html", data)


# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    return render(request, "HoardingBooker/failure.html", data)

def dremovecart(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = int(request.GET.get('id'))
        print(id)
        query = "delete from daddtocart WHERE ddcartid='%d'" % (id)
        cursor.execute(query)
        print(query)
        conn.commit()
        return payment(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def premovecart(request):
    try:

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        id = int(request.GET.get('id'))
        print(id)
        query = "delete from paddtocart WHERE pcartid='%d'" % (id)
        cursor.execute(query)
        print(query)
        conn.commit()
        return payment(request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def makeorder(request):
    try:
        cname = request.POST.get('name')
        mobno = int(request.POST.get('mobno'))
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        addresstype = request.POST.get('addresstype')
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        query = "insert into makeorder (cname,mobno,landmark,city,addresstype) VALUES('%s','%s','%s','%s','%s') " % (
            cname, mobno, landmark, city, addresstype)
        cursor.execute(query)
        print(query)
        conn.commit()
        return render(request, 'HoardingBooker/payment1.html', {'rows': rows, 'rows1': rows1, })
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()





def feedback(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()

    q = "SELECT * FROM category"
    cursor.execute(q)
    rows = cursor.fetchall()
    print(rows)
    q = "SELECT * FROM category1"
    cursor.execute(q)
    rows1 = cursor.fetchall()

    return render(request, 'HoardingBooker/feedback.html', {'rows': rows, 'rows1': rows1})


def searchdesign(request):
    print("hello")
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    data = request.GET.get('search')
    print(data)
    q = "select * from designdetails WHERE dname like '%%%s%%'" % data
    cursor.execute(q)
    print(q)
    rows2 = cursor.fetchall()
    print(rows2)
    msg = """<html>
      <div class="w3ls_w3l_banner_nav_right_grid1">
                <h6></h6>"""

    for i in rows2:
        print("hi")
        id = print(i[0])
        pic = print(i[1])
        name = print(i[2])
        size = print(i[3])
        type = print(i[4])
        price = print(i[7])
        """
        <div class="col-md-3 w3ls_w3l_banner_left">
            <div class="hover14 column">
                <div class="agile_top_brand_left_grid w3l_agile_top_brand_left_grid">
                    <div class="agile_top_brand_left_grid_pos">
                        <img src={% static "HoardingBooker/images/offer.png" %}  alt=""
                                         class="img-responsive"/>
                    </div>
                <div class="agile_top_brand_left_grid1">
                        <figure>
                            <div class="snipcart-item block">
                            <div class="snipcart-thumb" id="data">
                            <a href="\myproject\viewddetails?id=""" + id + """ "><img src=" """ + pic + """ " alt=""
                                                                                                    class="img-responsive"
                                                                                                    style="width: 350px;height: 200px"/></a><p> """ + type + """</p>

                                                <p>""" + size + """</p>
                                                <h4>INR """ + price + """</h4>

                                            </div>

                                            <div class="snipcart-details">

                                                <form action="\myproject\favouritedesign" method="get">
                                                    <fieldset>
                                                        <input type="hidden" value=" """ + id + """ " name="did">
                                                        <input type="submit" name="submit" value="Favourite"
                                                               class="button"/>
                                                    </fieldset>
                                                </form>
                                                <form action="\myproject\daddtocart" method="get">
                                                    <fieldset>
                                                        <input type="hidden" value=" """ + id + """ " name="did">
                                                        <input type="hidden" value=" """ + name + """ " name="name">
                                                        <input type="hidden" value=" """ + price + """ " name="price">
                                                        <input type="submit" name="submit" value="add to cart"
                                                               class="button" style="margin-top: 10px"/>
                                                    </fieldset>
                                                </form>
                                            </div>
                                        </div>
                                    </figure>
                                </div>
                            </div>
                        </div>
                    </div>"""

        if msg is not None:
            """<script>
                alert (" """ + msg + """ ")
                </script>

        <div class="clearfix"></div>
        </div>
    </html>"""
    f = open("categorywisedesign.html", 'w')
    f.write(msg)
    f.close()
    print(msg)
    return HttpResponse(msg)


def search(request):
    name = request.POST.get('name')
    print(name)
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        row = cursor.fetchall()

        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        q = "select * from designdetails WHERE dname like '%%%s%%'" % name
        cursor.execute(q)
        rows = cursor.fetchall()
        print(rows)
        if (rows == []):
            msg = "Result Not Found"
            print(msg)
            return render(request, 'HoardingBooker/search.html', {'rows': rows, 'row': row, 'msg': msg, 'rows1': rows1})
        else:
            return render(request, 'HoardingBooker/search.html', {'rows': rows, 'row': row, 'rows1': rows1})
        conn.commit()

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def searchp(request):
    area = request.POST.get('area')
    print(area)
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        row = cursor.fetchall()

        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        q = "select * from placedetails WHERE parea like '%%%s%%'" % area
        cursor.execute(q)
        rows = cursor.fetchall()
        print(rows)

        if (rows == []):
            msg = "Result Not Found"
            print(msg)
            return render(request, 'HoardingBooker/searchp.html',
                          {'rows': rows, 'row': row, 'msg': msg, 'rows1': rows1})
        else:
            print("sh")
            return render(request, 'HoardingBooker/searchp.html', {'rows': rows, 'row': row, 'rows1': rows1})

        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def search2(request):
    name = request.POST.get('name')

    print(name)
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        row = cursor.fetchall()

        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        q = "select * from designdetails WHERE dname like '%%%s%%'" % name
        cursor.execute(q)
        ddata = cursor.fetchall()
        print(ddata)
        q1 = "select * from placedetails WHERE parea like '%%%s%%'" % name
        cursor.execute(q1)
        pdata = cursor.fetchall()
        print(pdata)

        return render(request, 'HoardingBooker/search2.html',
                      {'row': row, 'rows1': rows1, 'ddata': ddata, 'pdata': pdata})
        conn.commit()

    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def feedback1(request):
    try:
        id = int(request.session.get('lid'))
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        now = datetime.datetime.now()
        print(now)

        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()

        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()
        print(rows)
        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        query = "insert into feedback(subject , message , date , customerid ) VALUES('%s','%s','%s','%d') " % (
            subject, message, now, id )
        cursor.execute(query)
        print(query)
        conn.commit()
        return render(request, 'HoardingBooker/feedback.html', {'rows': rows, 'rows1': rows1})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def viewfeedback(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
        cursor = conn.cursor()
        q = "SELECT * FROM category"
        cursor.execute(q)
        rows = cursor.fetchall()

        q = "SELECT * FROM category1"
        cursor.execute(q)
        rows1 = cursor.fetchall()

        q = "SELECT feedback.fid,login.uname,feedback.subject,feedback.message,feedback.date FROM login join feedback on login.lid=feedback.customerid  "
        cursor.execute(q)
        data = cursor.fetchall()

        return render(request, 'HoardingBooker/viewfeedback.html', {'rows': rows, 'rows1': rows1, 'data': data})
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def service(request):
    return render(request, 'HoardingBooker/service.html')


def about(request):
    return render(request, 'HoardingBooker/about.html')


def offer(request):
    return render(request, 'HoardingBooker/offer.html')

def suggestion(request):
    conn = mysql.connector.connect(host='localhost', database='hoardingbooker', user='root', password='root')
    cursor = conn.cursor()
    id = request.GET.get('lid')
    q = "select cintrest from custreg WHERE loginid1='%d'" % (id)
    type = cursor.execute(q)
    print(type)
    q1 = "SELECT * FROM designdetails  where designdetails.dtype= '%s'" % (type)
    cursor.execute(q1)
    rows2 = cursor.fetchall()

    return render(request, 'HoardingBooker/custindex.html', {'data': rows2})