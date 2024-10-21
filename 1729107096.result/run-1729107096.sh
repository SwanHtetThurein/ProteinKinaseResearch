#!/bin/sh
#$ -S /bin/bash
#$ -v PATH=:/opt/cd-hit:/opt/cd-hit/cd-hit-auxtools:/opt/cd-hit/psi-cd-hit:/opt/ncbi-blast-2.8.1+/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin



#$ -e /opt/data/1729107096/1729107096.err
#$ -o /opt/data/1729107096/1729107096.out
cd /opt/data/1729107096
sed -i "s/\x0d/\n/g" 1729107096.fas.0

faa_stat.pl 1729107096.fas.0

/opt/cd-hit/cd-hit -i 1729107096.fas.0 -d 0 -o 1729107096.fas.1 -c 0.9 -n 5  -G 1 -g 1 -b 20 -l 10 -s 0.0 -aL 0.0 -aS 0.0 -T 4 -M 32000
faa_stat.pl 1729107096.fas.1
/opt/cd-hit/clstr_sort_by.pl no < 1729107096.fas.1.clstr > 1729107096.fas.1.clstr.sorted
/opt/cd-hit/clstr_list.pl 1729107096.fas.1.clstr 1729107096.clstr.dump
gnuplot1.pl < 1729107096.fas.1.clstr > 1729107096.fas.1.clstr.1; gnuplot2.pl 1729107096.fas.1.clstr.1 1729107096.fas.1.clstr.1.png
/opt/cd-hit/clstr_list_sort.pl 1729107096.clstr.dump 1729107096.clstr_no.dump
/opt/cd-hit/clstr_list_sort.pl 1729107096.clstr.dump 1729107096.clstr_len.dump len
/opt/cd-hit/clstr_list_sort.pl 1729107096.clstr.dump 1729107096.clstr_des.dump des
tar -zcf 1729107096.result.tar.gz * --exclude=*.dump --exclude=*.env
echo hello > 1729107096.ok
