# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
#!/bin/bash

TINY=`wget -q "http://tinyurl.com/api-create.php?url=$1" -O -`
echo ${TINY} | xclip
echo -e "Shortened url : ${TINY}, copied to X clipboard"
