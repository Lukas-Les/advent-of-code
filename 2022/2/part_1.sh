#!/bin/bash

DRAW=3
WIN=6
result=0

solve () {
  local score=0
  local me=${2//$'\r'}
  if [ "$me" == "X" ]; then
    score=1
    if [ "$1" = "A" ]; then
      (( result += score + DRAW ))
    elif [ "$1" == "B" ]; then
      (( result += score ))
    elif [ "$1" == "C" ]; then
      (( result += score + WIN ))
    fi

  elif [ "$me" == "Y" ]; then
    score=2
    if [ "$1" == "B" ]; then
      (( result += score + DRAW ))
    elif [ "$1" == "A" ]; then
      (( result += score + WIN ))
    elif [ "$1" == "C" ]; then
        (( result += score ))
    fi

  elif [ "$me" == "Z" ]; then
    score=3
    if [ "$1" == "C" ]; then
      (( result += score + DRAW ))
    elif [ "$1" == "A" ]; then
      (( result += score ))
    elif [ "$1" == "B" ]; then
      (( result += score + WIN ))
    fi
  fi
}

while read -r elf me; do
  solve "$elf" "$me"
done < task_input.txt

echo "$result"
