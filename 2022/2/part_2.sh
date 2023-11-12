#!/bin/bash

DRAW=3
WIN=6

A_SCORE=1
B_SCORE=2
C_SCORE=3

result=0

solve () {
  local elf=$1
  local path=${2//$'\r'}

  echo "result = $result"

  case $elf in
    A)
      case $path in
        X)
          echo "$result + $C_SCORE"
          (( result += C_SCORE ))
          ;;
        Y)
          echo "$result + $DRAW + $A_SCORE"
          (( result += DRAW + A_SCORE ))
          ;;
        Z)
          echo "$result + $WIN + $B_SCORE"
          (( result += WIN + B_SCORE ))
          ;;
        esac ;;
    B)
      case $path in
        X)
          echo "$result + $A_SCORE"
          (( result += A_SCORE ))
          ;;
        Y)
          echo "$result + $DRAW + $B_SCORE"
          (( result += DRAW + B_SCORE ))
          ;;
        Z)
          echo "$result + $WIN + $C_SCORE"
          (( result += WIN + C_SCORE ))
          ;;
        esac ;;
    C)
      case $path in
        X)
          echo "$result + $B_SCORE"
          (( result += B_SCORE ))
          ;;
        Y)
          echo "$result + $DRAW + $C_SCORE"
          (( result += DRAW + C_SCORE ))
          ;;
        Z)
          echo "$result += $WIN + $A_SCORE"
          (( result += WIN + A_SCORE ))
          ;;
        esac ;;
    esac
}

while read -r elf path; do
  solve "$elf" "$path"
done < task_input.txt

echo "$result"
