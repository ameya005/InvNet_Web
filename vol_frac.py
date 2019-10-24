import numpy as np
DIM = 128

def cal_vol_fraction(images):
    channelList = [0, 1, 2, 3, 4, 5]

    VF_ch0, VF_ch1, VF_ch2, VF_ch3, VF_ch4, VF_ch5 = 0, 0, 0, 0, 0, 0
    for i in range(len(images)):
        ch0 = len(np.where(images[i] == channelList[0])[0])
        ch1 = len(np.where(images[i] == channelList[1])[0])
        ch2 = len(np.where(images[i] == channelList[2])[0])
        ch3 = len(np.where(images[i] == channelList[3])[0])
        ch4 = len(np.where(images[i] == channelList[4])[0])
        ch5 = len(np.where(images[i] == channelList[5])[0])

        VF_ch0 += ch0 / (DIM ** 2)
        VF_ch1 += ch1 / (DIM ** 2)
        VF_ch2 += ch2 / (DIM ** 2)
        VF_ch3 += ch3 / (DIM ** 2)
        VF_ch4 += ch4 / (DIM ** 2)
        VF_ch5 += ch5 / (DIM ** 2)

    VF_ch0 = VF_ch0 / len(images)
    VF_ch1 = VF_ch1 / len(images)
    VF_ch2 = VF_ch2 / len(images)
    VF_ch3 = VF_ch3 / len(images)
    VF_ch4 = VF_ch4 / len(images)
    VF_ch5 = VF_ch5 / len(images)

    return round(VF_ch0, 2), round(VF_ch1, 2), round(VF_ch2, 2), round(VF_ch3, 2), round(VF_ch4, 2)