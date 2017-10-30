#!/bin/bash
while :
do
	RESPONSE=$(curl http://localhost:5000/os)
	echo $RESPONSE
	sleep 2
done
