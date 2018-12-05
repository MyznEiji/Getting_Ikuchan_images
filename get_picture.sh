#!/bin/bash

while read line
do
  curl -s -O -l  $line
done < ./images_url.txt

mv *.jpeg img/
mv *.png img/
mv *.gif img/
