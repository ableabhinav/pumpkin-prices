csv_dir=/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/
cd $csv_dir

for k in `ls -ltr *[.csv,.CSV] | awk '{print $9}'`
	do
		for j in `grep -Po '[0-9]+/[0-9]+/[0-9]+' $k`
			do
				echo $j
				if [[ ! -z "$j" ]]; then
					newdate=$(date -d"$j" "+%Y-%m-%d")
					sed -i "s#$j#$newdate#" $k
				fi
			done
done
 
