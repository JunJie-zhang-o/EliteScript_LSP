
import sys
from pyls import __main__

with open("log.log", "w+", encoding="utf-8") as f:
    f.write()


sys.argv.append("--tcp")
sys.argv.append("--log-file=log.log")


__main__.main()