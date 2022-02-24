FILE_A:="a_an_example.in.txt"
FILE_B:="b_better_start_small.in.txt"
FILE_C:="c_collaboration.in.txt"
FILE_D:="d_dense_schedule.in.txt"
FILE_E:="e_exceptional_skills.in.txt"
FILE_F:="f_find_great_mentors.in.txt"

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
run-f:
	python3 main.py input/${FILE_F}
zip:
	zip -r sources.zip *.py utils