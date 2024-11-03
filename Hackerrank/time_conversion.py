import os

def timeConversion(s):
    print(s)
    d = int(s[:2:])
    if "PM" in s:
        s_ = str(12 + d) + ":" + s[3:-2:]
    else:
        if d < 12:
            s_ = s[:-2:]
        else:
            s_ = str(abs(d - 12)) + ":" + s[3:-2:]


    if len(s_)%2 != 0 :
        return "0"+s_
    elif "24" in s_[:2:]:
        return s[:-2:]
    else:
        return s_

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

