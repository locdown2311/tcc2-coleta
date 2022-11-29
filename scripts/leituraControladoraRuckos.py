import pandas as pd

from datetime import datetime


def main():
    input = 'all_controladora_ruckos.txt'
    with open(input) as f:
        txt = f.readlines()


    n = len(txt)

    for i in range(n):

        txt[i] = txt[i].strip()

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    col9 = []
    col10 = []
    col11 = []
    col12 = []
    col13 = []
    for i in range(n):

        line = txt[i].split(' ')[0]
        dt = datetime.fromisoformat(line)
        # DATA
        col1.append(dt)
        # IP
        line = txt[i].split(' ')[1:9]
        col2.append(line[0])
        # EVENTO
        line = txt[i].split(' ')
        col3.append(line[3])
        # MAC
        line = txt[i].split(' ')
        col4.append(line[6])
        line = txt[i].split(' ')
        rx_rssi = line[7].split(',')[0]
        # print(rx_rssi)
        rssi_split = rx_rssi.split('=')[1]
        col5.append(rssi_split)
        ack = line[7].split(',')[1]
        ack_split = ack.split('=')[1]
        col6.append(ack_split)
        reason = line[7].split(',')[2]
        reason_split = reason.split('=')[1]
        col7.append(reason_split)
        freq = line[7].split(',')[3]
        freq_split = freq.split('=')[1]
        col8.append(freq_split)
        chan = line[7].split(',')[4]
        chan_split = chan.split('=')[1]
        col9.append(chan_split)

if __name__ == '__main__':
    main()
