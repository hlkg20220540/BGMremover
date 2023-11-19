import wavio
import os
from threading import Thread

DrySoundData0 = []
DrySoundData1 = []
DrySoundData2 = []
DrySoundData3 = []
DrySoundData4 = []
DrySoundData5 = []
DrySoundData6 = []
DrySoundData7 = []

def partTMain():
    global DrySoundDataTMain
    for i in range(int(len(FullMusic.data)/8*1),int(len(FullMusic.data)/8*1+3*FullMusic.rate),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundDataTMain.append(DryUnit)
        print(DryUnit)
    return DrySoundDataTMain

def partTXL(step):
    global DrySoundDataTXL
    for i in range(int(len(FullMusic.data)/8*1),int(len(FullMusic.data)/8*1+3*FullMusic.rate),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix-step]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundDataTXL.append(DryUnit)
        print(DryUnit)
    return DrySoundDataTXL

def partTXR(step):
    global DrySoundDataTXR
    for i in range(int(len(FullMusic.data)/8*1),int(len(FullMusic.data)/8*1+3*FullMusic.rate),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix+step]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundDataTXR.append(DryUnit)
        print(DryUnit)
    return DrySoundDataTXR

def part0():
    global DrySoundData0
    for i in range(0,int(len(FullMusic.data)/8*1),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData0.append(DryUnit)
        print(DryUnit)
    return DrySoundData0

def part1():
    global DrySoundData1
    for i in range(int(len(FullMusic.data)/8*1),int(len(FullMusic.data)/8*2),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData1.append(DryUnit)
        print(DryUnit)
    return DrySoundData1

def part2():
    global DrySoundData2
    for i in range(int(len(FullMusic.data)/8*2),int(len(FullMusic.data)/8*3),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData2.append(DryUnit)
        print(DryUnit)
    return DrySoundData2

def part3():
    global DrySoundData3
    for i in range(int(len(FullMusic.data)/8*3),int(len(FullMusic.data)/8*4),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData3.append(DryUnit)
        print(DryUnit)
    return DrySoundData3

def part4():
    global DrySoundData4
    for i in range(int(len(FullMusic.data)/8*4),int(len(FullMusic.data)/8*5),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData4.append(DryUnit)
        print(DryUnit)
    return DrySoundData4

def part5():
    global DrySoundData5
    for i in range(int(len(FullMusic.data)/8*5),int(len(FullMusic.data)/8*6),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData5.append(DryUnit)
        print(DryUnit)
    return DrySoundData5

def part6():
    global DrySoundData6
    for i in range(int(len(FullMusic.data)/8*6),int(len(FullMusic.data)/8*7),1):
        FullUnit = FullMusic.data[i+FullFix]
        BGUnit = BGMusic.data[i+BGfix]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData6.append(DryUnit)
        print(DryUnit)
    return DrySoundData6

def part7():
    global DrySoundData7
    for i in range(int(len(FullMusic.data)/8*7),len(FullMusic.data),1):
        try:
            FullUnit = FullMusic.data[i+FullFix]
        except:
            FullUnit = [0,0]
        try:
            BGUnit = BGMusic.data[i+BGfix]
        except:
            BGUnit = [0,0]
        DryUnit0 = FullUnit[0] - BGUnit[0]
        DryUnit1 = FullUnit[1] - BGUnit[1]
        DryUnit = [DryUnit0,DryUnit1]
        DrySoundData7.append(DryUnit)
        print(DryUnit)
    return DrySoundData7
Process0 = Thread(target=part0)
Process1 = Thread(target=part1)
Process2 = Thread(target=part2)
Process3 = Thread(target=part3)
Process4 = Thread(target=part4)
Process5 = Thread(target=part5)
Process6 = Thread(target=part6)
Process7 = Thread(target=part7)

print('请拖入完整wav并回车。')
filepath = input()
if ('"' in filepath):
    filepath = filepath.replace('"','')
FullMusic = wavio.read(filepath)
MusicName = os.path.basename(filepath)
MusicName = MusicName.replace('.','干声.')
MusicChannel = FullMusic.sampwidth
del filepath

print('请拖入伴奏wav并回车。')
filepath = input()
if ('"' in filepath):
    filepath = filepath.replace('"','')
BGMusic = wavio.read(filepath)
del filepath

BGfix = 0
FullFix = 0
FixSetOK = 'width'
while FixSetOK != 'ok':
    DrySoundDataTMain = []
    DrySoundDataTXL = []
    DrySoundDataTXR = []
    BGfix = int(input('伴奏修正值:'))
    if BGfix < 0:
        FullFix = -BGfix
        BGfix = 0
    if FixSetOK == 'width':
        TestStep = FullMusic.rate
    if FixSetOK == 'thin':
        TestStep = int(input('请输入预览跨度：'))
    if FixSetOK == '':
        TestStep = laststep
    partTXL(step=TestStep)
    partTMain()
    partTXR(step=TestStep)
    DrySoundDataT = DrySoundDataTXL + DrySoundDataTMain + DrySoundDataTXR
    wavio.write('test.wav',DrySoundDataT,FullMusic.rate,None,FullMusic.sampwidth)
    os.system('start test.wav')
    laststep = TestStep
    FixSetOK = input('请试听并选择下一步的模式（""、width、thin、ok）：')

Process0.start()
Process1.start()
Process2.start()
Process3.start()
Process4.start()
Process5.start()
Process6.start()
Process7.start()
Process0.join()
Process1.join()
Process2.join()
Process3.join()
Process4.join()
Process5.join()
Process6.join()
Process7.join()
DrySoundData = DrySoundData0 + DrySoundData1 + DrySoundData2 + DrySoundData3 + DrySoundData4 + DrySoundData5 + DrySoundData6 + DrySoundData7

wavio.write(MusicName,DrySoundData,FullMusic.rate,None,FullMusic.sampwidth)
input('导出成功：'+MusicName)