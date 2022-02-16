FILE_A:="a_an_example.in.txt"
FILE_B:="b_basic.in.txt"
FILE_C:="c_coarse.in.txt"
FILE_D:="d_difficult.in.txt"
FILE_E:="e_elaborate.in.txt"

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