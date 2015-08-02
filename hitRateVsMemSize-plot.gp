set terminal svg size 600,400 dynamic enhanced fname 'arial'  fsize 10 mousing name 'hitRates' butt dashlength 1.0 
set output 'hitRateVsMemSize.svg'
#set terminal postscript eps size 600,400 enhanced color font 'Helvetica,20' linewidth 2
#set output 'hitRateVsMemSize.eps'
set boxwidth 0.9 absolute
set style fill   solid 1.00 border lt -1
set datafile missing '-'
#set xtics border in scale 0,0 nomirror rotate by -45  autojustify
#set xtics norangelimit
#set xtics ()
#set bars 0.5
set grid ytics lw 0.5 lc rgb "#868686"
set xlabel "Tamaño de Memoria (Mb)"
set ylabel "Tasa de Aciertos (%)"
#set linetype 1 lc rgb 'black'
#set linetype 2 lc rgb '#555555'
#set linetype 3 lc rgb '#999999'
set datafile separator ',' 
plot 'hitRateVsMemSize.dat' u 2:xtic(1) with lines lw 3 title columnheader, \
     'hitRateVsMemSize.dat' u 3:xtic(1) with lines lw 3 title columnheader, \
     'hitRateVsMemSize.dat' u 4:xtic(1) with lines lw 3 title columnheader, \
     'hitRateVsMemSize.dat' u 5:xtic(1) with lines lw 3 title columnheader
