
import sys

def simInt(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print("Simple Interest:", simInt(p, i, t))
