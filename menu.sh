a="\033[30;1m"
m="\033[31;1m"
h="\033[32;1m"
k="\033[33;1m"
b="\033[34;1m"
r="\033[35;1m"
c="\033[36;1m"
p="\033[37;1m"
o="\033[0;37m"


clear
echo "
$m+$k----------------------------------------$m+
$a   /\___/\ $c  ╦ ╦┌─┐┬  ┌─┐ ╔╦╗┌─┐┌─┐┬  ┌─┐
$a  /       \ $c ║║║│ ││  ├┤───║ │ ││ ││  └─┐
$a  / .\ /. \ $c ╚╩╝└─┘┴─┘└    ╩ └─┘└─┘┴─┘└─┘
$a  \\ | | //$m  +$b---------------------------$m+
$a    \(o)/  $p  Author $m :$r Tn.YuT7-CrAb
$o      U    $p  Version$m :$h 1.00
$m+$k----------------------------------------$m+

$p [${m}01$p]$h TOMBOL SPESIAL TERMUX
$p [${m}02$p]$h SPAM SMS MAPCLUB ( unli )
$p [${m}03$p]$h SPAM SMS TRI ( unli )
$p [${m}04$p]$h SPAM CALL v1
$p [${m}05$p]$h ENCRYPT BASH
$p [${m}06$p]$h ENCRYPT MARSHAL
$p [${m}07$p]$h CEK ALAMAT IP ANDA
$p [${m}00$p]$h EXIT TOOLS
"
echo -n "$p[$m!$p] ${b}Pilih$m :$k "
read bcs;

if [ $bcs = "1" ] || [ $bcs = "01" ]; then
cd data1
python2 tombol.py

elif [ $bcs = "2" ] || [ $bcs = "02" ]; then
cd data1
python2 mapclub.py

elif [ $bcs = "3" ] || [ $bcs = "03" ]; then
cd data1
php tri.php

elif [ $bcs = "4" ] || [ $bcs = "04" ]; then
cd data1
sh call1.sh

elif [ $bcs = "5" ] || [ $bcs = "05" ]; then
cd data1
python2 encript.py

elif [ $bcs = "6" ] || [ $bcs = "06" ]; then
cd data1
python2 marshal.py

elif [ $bcs = "7" ] || [ $bcs = "07" ]; then
cd data1
python2 ip.py

elif [ $bcs = "0" ] || [ $bcs = "00" ]; then
exit

else
echo "$p[$m!$p]$m Pilih yang bener$b..."
sh menu.sh
fi
