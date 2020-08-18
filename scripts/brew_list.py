import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        print("Error: must pass in name of output file when calling script")
        return -1

    print("Querying brew packages...")

    proc = subprocess.Popen(["brew", "list"], stdout=subprocess.PIPE)
    out = str(proc.communicate()[0])
    out = out[2:len(out) - 1]

    print("Got list of packages...")

    filename = sys.argv[1]

    with open(filename, "w") as f:
        i = 0
        while i < len(out):
            if out[i] == "\\":
                f.write("\n")
                i += 2
            else:
                f.write(out[i])
                i += 1

    print(f"Wrote package list to {filename}")
    return 0


if __name__ == "__main__":
    main()

