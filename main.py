import clipboard as c
import os
def main():
    p = [c.paste()]
    clear = lambda : os.system("cls")
    p = p[:0] + p[0:]
    print("start")
    while True:
        i = c.paste()
        if i != p[len(p) - 1]:
            p.append(i)
            clear()
            for o in p:
                if o != None:
                    print(o)
if __name__ == '__main__':
    main()