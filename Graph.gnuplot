set terminal png size 3000,1500
set output "5000.png"
set datafile separator " "
set xtics  0,10
unset colorbox
set xrange [-5:128]
set yrange [0:70000]
set cbrange[70:90]
set palette defined (0 'blue', 50 'green',  100 'red')
set logscale y
set xlabel "Time(Months)"
set ylabel "Price($)"

plot "combi.txt" using 1:3:2 notitle palette pt 7 lw 5 with lines, \
"combi.txt" using 1:3:2 notitle palette pt 7 ps 5
