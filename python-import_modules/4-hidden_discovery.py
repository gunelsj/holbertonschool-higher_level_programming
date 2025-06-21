#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sys.path.append('/tmp')
    import hidden_4

    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
