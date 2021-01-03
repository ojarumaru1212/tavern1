#!/bin/bath

case $# in
  0)
    echo "全機能のテストを実行します。"
    pytest -vv >> log2.txt
    ;;
  1)
    echo "$1のテストを実行します。"
    pytest -v -s test_$1.tavern.yaml >> log2.txt
    ;;
  *)
    echo "引数は1つまでです！"
    ;;
esac

array=($(grep FAILED log2.txt))

if [ -z "$array" ]; then
    echo "Array empty"
else
    echo "Array non empty"
fi

if test $? -ne 0
  then 
    echo "異常終了しました。"
fi