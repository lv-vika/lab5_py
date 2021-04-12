import re


START_DATE = r"01/Jul/1995:05:39"
END_DATE = r"01/Jul/1995:07:55"

if __name__ == '__main__':

    with open('access_log_Jul95.txt', 'r') as log:
        log_file = log.readlines()

    errors_counter = 0
    is_right_date = False

    for line in log_file:
        if None != re.search(START_DATE, line):
            is_right_date = True
        else:
            pass

        if is_right_date and None != re.match(r".*(GET).*html.*(\" [^(20)]).*", line):
            errors_counter += 1

        if None != re.search(END_DATE, line):
            is_right_date = False
            break

    print(f"{errors_counter} html GET errors between {START_DATE} and {END_DATE} found")
