import pandas as pd

from datetime import datetime


def main():
    input = 'dados_input_ruckos.csv'
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
        # RX_RSSI
        rx_pkt = line[9].split('(')[1]
        # print(rx_pkt)
        # RX_PKT
        rx_split = rx_pkt.split(',')[0]
        # print(rx_split)
        # BYTE_RX
        byterx_split = rx_pkt.split(',')[1]
        # TX_PKT
        tx_pkt = rx_pkt.split(',')[2]
        # BYTE_TX
        bytetx_split = rx_pkt.split(',')[3]

        col10.append(rx_split)
        col11.append(byterx_split)
        col12.append(tx_pkt)
        bytetx_split = bytetx_split[:-1]
        col13.append(bytetx_split)


    df = pd.DataFrame([col1, col2, col3, col4, col5, col6, col7,
                    col8, col9, col10, col11, col12, col13]).T
    #df = df.T

    df.columns = ['datetime', 'router', 'event', 'mac', 'rssi', 'ack',
                'reason', 'freq', 'chan', 'rx_pkt', 'byte_rx', 'tx_pkt', 'byte_tx']
    df.to_csv('input_ruckos_form.csv', mode='a',index=False)


if __name__ == "__main__":
    main()
