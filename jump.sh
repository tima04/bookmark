#!/usr/bin/env bash

if [ $# = 2 ]; then
	$(jump.py $1 $2)
else  
	if [ "$1" != "s" ]; then
		dir=$(jump.py $1)
		echo $dir
		cd $dir
	else
		# echo $(jump.py s)
		echo $(jump.py s) | sed 's/,/\n/g'
	fi
fi
