FILE_A:="a_example.txt"
FILE_B:="a_example.txt"
FILE_C:="a_example.txt"
FILE_D:="a_example.txt"
FILE_E:="a_example.txt"

run-a:
	python3 main.py input/${FILE_A}
run-b:
	python3 main.py input/${FILE_B}
run-c:
	python3 main.py input/${FILE_C}
run-d:
	python3 main.py input/${FILE_D}
run-e:
	python3 main.py input/${FILE_E}

zip:
	zip -r sources.zip *.py utils