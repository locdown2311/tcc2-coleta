import pandas as pd

from datetime import datetime
def main():
    input = 'dados_hostapd_ubi.csv'
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
        #DATA
        col1.append(dt)
        #IP
        line = txt[i].split(' ')[1:9]
        #EVENTO
        col2.append(line[0])
        line = txt[i].split(' ')
        #MAC
        col3.append(line[3])
        line = txt[i].split(' ')
        col4.append(line[7])
        line = txt[i].split(' ')
        rx_rssi = line[8].split(',')[0]
        rssi_split = rx_rssi.split('=')[1]
        ack = line[8].split(',')[1]
        ack_split = ack.split('=')[1]
        reason = line[8].split(',')[2]
        reason_split = reason.split('=')[1]
        freq = line[8].split(',')[3]
        freq_split = freq.split('=')[1]
        chan = line[8].split(',')[4]
        chan_split = chan.split('=')[1]
        #RX_RSSI
        col5.append(rssi_split)
        #ACK
        col6.append(ack_split)
        #REASON
        col7.append(reason_split)
        #FREQ
        col8.append(freq_split)
        #CHAN
        col9.append(chan_split)
        rx_pkt = line[10].split('(')[1]
        # RX_PKT
        rx_split = rx_pkt.split(',')[0]
        # BYTE_RX
        byterx_split = rx_pkt.split(',')[1]
        # TX_PKT
        tx_pkt = rx_pkt.split(',')[2]
        # BYTE_TX
        bytetx_split = rx_pkt.split(',')[3]
        
        col10.append(rx_split)
        col11.append(byterx_split)
        col12.append(tx_pkt)
        

        # remove the last position of bytetx_split
        bytetx_split = bytetx_split[:-1]
        col13.append(bytetx_split)


    df = pd.DataFrame([col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13])
    df = df.T

    df.columns=['datetime','router','event_description','mac','rx_rssi','ack_rssi','reason','freq','chan','rx_pkt','byte_rx','tx_pkt','byte_tx']
    df.to_csv('send_ruckus_form.csv',mode='a', index=False)


if __name__ == "__main__":
    main()
