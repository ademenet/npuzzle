test_errors()
{
    python main.py tests/error_alpha_lines
    python main.py tests/error_blank_file
	for i in {1..3}
	do
        python main.py tests/error_blank_lines$i
	done
	for i in {1..2}
	do
        python main.py tests/error_row_size$i
	done
	for i in {1..7}
	do
        python main.py tests/error_unsolvable$i
	done    
    python main.py tests/error_wrong_size
}


test_valids()
{
	for i in {1..3}
	do
        python main.py tests/test30$i
	done
    python main.py tests/test401
}


while true; do
	echo "\033[34;1mChoose a tests suite:\n
		[1]\tErrors tests suite\n
		[2]\tValid tests suite\n
		[q]\tQuit\n
		\033[0m"
	read tests
	case $tests in
		"1" )		test_errors ;;
		"2" )		test_valids ;;
		"q" )		exit ;;
	esac
done