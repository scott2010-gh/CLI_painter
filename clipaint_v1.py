import os
import time as t
global size,x,y,sym,brush
print('CLI Paint! v1.0-beta  [for windows]')
try:
    import keyboard
except:
    print('Installing keyboard library on computer...')
    os.system('pip install keyboard')
    try:
        import keyboard
        print('Successfully installed! Please restart the program.')
    except:
        print("Can't install keyboard module... please check python pip.")
brush_list = ['■','▤','▥','▦','▩','●']
paint = []
x=0
y=0
sym='◇'
brush = '■'
def save():
    os.system('cls')
    title = str(input("Enter title : "))
    savefile = open("CLI_paint.txt",'w')
    for i in range(len(paint)):
        savefile.write(paint[i]+"\n")
def set():
    global x,y,brush
    for i in range(len(paint)):
        if i==y:
            paint[i] = paint[i][:x]+brush+paint[i][x+1:]
def refresh():
    os.system('cls')
    global size,x,y,sym,brush
    if paint[y][x] in brush_list:
        sym='◆'
    else:
        sym='◇'
    for i in range(len(paint)):
        if i==y:
            if x==0:
                print(sym+paint[i][1:])
            else:
                fr = paint[i][:x]
                bk = paint[i][x+1:]
                print(fr+sym+bk)
        else:
            print(paint[i])
    print('\n\n[ choose brush |  ■ ▤ ▥ ▦ ▩ ● □(eraser) ]    [S] to save')
size = str(input("Enter the size of your drawing board(ex : 30x30) >> "))
for i in range(int(size.split('x')[1])):
    paint.append('□'*int(size.split('x')[0]))

refresh()
while True:
    if keyboard.is_pressed('Left') and x>0:
        x-=1
        refresh()
        t.sleep(0.1)
    elif keyboard.is_pressed('Right') and x<int(size.split('x')[0])-1:
        x+=1
        refresh()
        t.sleep(0.1)
    elif keyboard.is_pressed('Up') and y>0:
        y-=1
        refresh()
        t.sleep(0.1)
    elif keyboard.is_pressed('Down') and y<int(size.split('x')[1])-1:
        y+=1
        refresh()
        t.sleep(0.1)
    elif keyboard.is_pressed('Enter'):
        set()
        refresh()
        t.sleep(0.1)
    elif keyboard.is_pressed('q'):
        brush = '■'
        t.sleep(0.1)
    elif keyboard.is_pressed('w'):
        brush = '▤'
        t.sleep(0.1)
    elif keyboard.is_pressed('e'):
        brush = '▥'
        t.sleep(0.1)
    elif keyboard.is_pressed('r'):
        brush = '▦'
        t.sleep(0.1)
    elif keyboard.is_pressed('t'):
        brush = '▩'
        t.sleep(0.1)
    elif keyboard.is_pressed('y'):
        brush = '●'
        t.sleep(0.1)
    elif keyboard.is_pressed('u'):
        brush = '□'
        t.sleep(0.1)
    elif keyboard.is_pressed('s'):
        save()
        break
