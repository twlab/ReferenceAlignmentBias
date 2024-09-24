#!/bin/bash
QueryReadCountFile=$1
RefReadCountFile=$2
queryName=$3
refName=$4
pathout=$5



paste $QueryReadCountFile $RefReadCountFile  > "$pathout"FinalTable"$refName"_"$queryName".txt
# querychr qstart qstop qread rchr rstart rstop rread
