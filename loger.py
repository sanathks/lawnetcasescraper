def write(filename, content):
    f = open("./dataset/" + filename + '.txt', 'w')
    f.write(content)
    f.close()


def log_ignored_case(link):
    with open("./ignored_case_log.txt", "a") as ignored_case_log:
        ignored_case_log.write(link+"\n")


def log_current_index(index):
    f = open("./last_index.txt", 'w')
    f.write(index)
    f.close()


def get_current_index():
    with open('./last_index.txt', 'r') as index_file:
        index = index_file.read()
    return int(index)
