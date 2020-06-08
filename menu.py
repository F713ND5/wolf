#_*_coding=UTF-8_*_

import subprocess as sp, os, sys, requests, random, json
from time import sleep

#warna
hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
gelap = '\x1b[0;37m'

h = '\x1b[1;92m'
c = '\x1b[1;96m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
p = '\x1b[1;97m'
b = '\x1b[1;94m'
m = '\x1b[1;91m'
g = '\x1b[0;37m'
a = '\x1b[1;30m'

def bersih():
	os.system('clear')

def banner():
	bersih()
	print '%s+%s----------------------------------------%s+'%(m,k,m)
	print '%s   /\___/\%s   ╦ ╦┌─┐┬  ┌─┐ ╔╦╗┌─┐┌─┐┬  ┌─┐'%(a,c)
	print '%s  /       \%s  ║║║│ ││  ├┤───║ │ ││ ││  └─┐'%(a,c)
	print '%s  / .\ /. \%s  ╚╩╝└─┘┴─┘└    ╩ └─┘└─┘┴─┘└─┘'%(a,c)
	print '%s  \\ | | //%s  +%s---------------------------%s+'%(a,m,b,m)
	print '%s    \(o)/  %s  Author %s :%s Tn.YuT7-CrAb'%(a,p,m,u)
	print '%s      U    %s  Version%s :%s 1.00'%(a,p,m,h)
	print '%s+%s----------------------------------------%s+'%(m,k,m)
	print ''

def main():
	banner()
	print '  %s[%s01%s]%s TOMBOL SPESIAL TERMUX'%(p,m,p,h)
	print '  %s[%s02%s]%s SPAM SMS MAPCLUB%s (%s unli%s )'%(p,m,p,h,k,u,k)
	print '  %s[%s03%s]%s SPAM SMS TRI%s (%s unli%s )'%(p,m,p,h,k,u,k)
	print '  %s[%s04%s]%s SPAM CALL'%(p,m,p,h)
	print '  %s[%s05%s]%s ENCRIPT BASH'%(p,m,p,h)
	print '  %s[%s06%s]%s ENCRIPT PYTHON%s (%s marshal%s )'%(p,m,p,h,k,u,k)
	print '  %s[%s07%s]%s CEK ALAMAT IP ANDA'%(p,m,p,h)
	print '  %s[%s08%s]%s SC DEFACE CREATOR%s (%s unli%s )'%(p,m,p,h,k,u,k)
	print '  %s[%s00%s]%s EXIT TOOLS'%(p,m,p,k)
	print ''
	ab = raw_input('%s  %s[%s!%s]%s Pilih %s:%s '%(m,p,m,p,b,m,k))


	if ab =='1' or ab =='01': #tombol spesial
		os.system('cd data1')
		os.system('python2 tombol.py')

	elif ab =='2' or ab =='02': #mapclub
		os.system('cd data1')
		os.system('python2 mapclub.py')

	elif ab =='3' or ab =='03': #tri
		os.system('cd data1')
                os.system('php tri.php')

	elif ab =='4' or ab =='04': #callv1
                os.system('cd data1')
                os.system('python2 call1.py')

	elif ab =='5' or ab =='05': #encript bash
                os.system('cd data1')
                os.system('python2 encript.py')

	elif ab =='6' or ab =='06': #encript marshal
                os.system('cd data1')
                os.system('python2 marshal.py')

	elif ab =='7' or ab =='07': #cek your ip
                os.system('cd data1')
                os.system('python2 ip.py')

	elif ab =='8' or ab =='08': #cDEFACE
		os.system('cd data1')
		os.system('python2 screator.py')
	else:
		print '%s [%s!%s]%s Pilih yang bener%s...'%(p,m,p,m,b)
		sleep(3)
		main()

main()
