import zipfile as zp
zip = zp.ZipFile('zipppd.zip','w')

zip.write('2nd.py')
zip.write('basic.py')
zip.write('new.py')