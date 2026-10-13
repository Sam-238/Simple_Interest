import sys 

def simInt(principal,interest,time):
    return (principal*interest*time)/100

if __name__ == "__main__"

p = int(sys.argv[1])
i = int(sys.argv[1])
t = int(sys.argv[1])

print("simple Interest:",simInt(p,i,t))