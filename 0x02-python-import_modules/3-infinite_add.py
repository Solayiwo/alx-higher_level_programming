#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    op_sum = 0
    for i in range(len(sys.argv) - 1):
        op_sum += int(sys.argv[i + 1])
    print("{}".format(op_sum))
