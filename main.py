# 把TXT文件转换为WAV声音
# 需要TXT文件中每一行代表一个采样数据，为十六进制或有符号的十进制

import numpy as np
import wave

def Txt2Wav(input, channel, depth, rate, output, hex):
    f = open(input)
    line = f.readline()  # 每次读出txt文件中的一行内容
    data = []  # 初始化一个空矩阵
    i = 0
    j = 0
    while line:  # 当未读到文件最后时
        try:
            # 字符串转整型
            if hex: 
                v = int(line,16)
                if v>0x7fff:
                    v = v + 0xff0000 - 0xffffff
                print(i, bytes(line, encoding='utf-8'), v)
            else:
                v = np.short(line)
            # 添加整型数据
            if v>0:
                data.append(v)  # 将从文件中读到的数据放入列表的两个中括号之间
            i += 1
        except:
            # 转换失败，跳过
            j += 1
            print(i + j, '行失败', line)
        # 读取下一行
        line = f.readline()
        # cnt = cnt+1
    # 关闭TXT文件
    f.close()
    wavdata = np.array(data)  # 将列表数据转换成数组
    print("文件行数(即采样点数)：成功：", i, '失败：', j)

    f = wave.open(output, "wb")  # 新建并打开wav文件
    # 配置声道数、量化位数和采样频率
    f.setnchannels(channel)  # 配置声道数
    f.setsampwidth(depth)  # 配置量化位数
    f.setframerate(rate)  # 配置采样频率
    f.writeframes(wavdata.tobytes())  # 将wav_data转换为二进制数据写入文件
    f.close()

if __name__ == "__main__":
    channel = 1 # 转换参数
    depth = 2 # 位深度
    rate = 8000 # 声音采样率
    fin = r'2.TXT' # 输入文件
    fout = r'2.wav' # 输出文件
    hex = False # 字符串为十六进制(True)还是十进制(False)

    print("声道数：", channel)
    print("量化位数：", depth)
    print("采样频率：", rate)
    
    Txt2Wav(fin, channel, depth, rate, fout, hex)
