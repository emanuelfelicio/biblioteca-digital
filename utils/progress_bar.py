import sys
from utils.ansi_colors import RESET, RED, GREEN, YELLOW, BLUE, CYAN, WHITE

def progress_bar(iterable, prefix="", size=60, file=sys.stdout):
    count = len(iterable)
    
    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "=" * x, " " * (size - x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(iterable):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()