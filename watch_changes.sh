#!/bin/bash

RASPBERRY=192.168.1.6
PREFIX_LEN=$((`pwd | wc -c` + 1))
fswatch client server | while read ABS_PATH
do
  # temporary files created by intellij when safe saving
  if [[ ${ABS_PATH} != *___jb_old___ ]] && [[ ${ABS_PATH} != *___jb_tmp___ ]] ;
  then
    PATH=`echo ${ABS_PATH} | cut -c ${PREFIX_LEN}-`
    if [[ ${PATH} == client/* ]] ;
    then
      webpack
    fi
    if [[ ${PATH} == server/* ]] ;
    then
      REMOTE_PATH=`echo ${PATH} | cut -c 8-`
      scp ${PATH} pi@${RASPBERRY}:/home/pi/blinky/${REMOTE_PATH}
      ssh pi@${RASPBERRY} sudo service blinky restart
      echo "Blinky @ ${RASPBERRY} restarted"
    fi
  fi
done
