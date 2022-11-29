import shutil


def inputRuckos(infile):
    important = []
    keep_phrases = ["ieee80211_input()"]

    with open(infile) as f:
        f = f.readlines()

    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    return important


def controladoraRuckos(infile):
    important = []
    keep_phrases = ["ieee80211_input()"]

    with open(infile) as f:
        f = f.readlines()

    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    return important


def hostapd(infile):
    important = []
    keep_phrases = ["hostapd"]

    with open(infile) as f:
        f = f.readlines()

    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break
    return important


def sendMsg(infile):
    important = []
    keep_phrases = ["ieee80211_send_mgmt()"]

    with open(infile) as f:
        f = f.readlines()

    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    return important


def leituraRadius(infile):
    important = []
    keep_phrases = ["DHCP", "Login"]

    with open(infile) as f:
        f = f.readlines()

    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    return important


if __name__ == '__main__':
    ipControladora = ['10.0.10.5']
    ipsRuckus = [
        '10.0.10.6',
        '10.0.10.29',
        '10.0.10.53',
        '10.0.10.56',
        '10.0.10.63',
        '10.0.10.68',
        '10.0.10.74',
        '10.0.10.76',
        '10.0.10.82',
        '10.0.10.101',
        '10.0.10.102',
        '10.0.10.186',
        '10.0.11.71',
        '10.0.11.77',
        '10.0.11.254',
    ]
    ipsUbi = [
        '10.0.11.6',
        '10.0.11.7',
        '10.0.11.8',
        '10.0.11.9',
        '10.0.11.10',
        '10.0.11.11',
        '10.0.11.12',
        '10.0.11.13',
        '10.0.11.15',
        '10.0.11.16',
        '10.0.11.17',
        '10.0.11.18',
        '10.0.11.19',
        '10.0.11.20',
        '10.0.11.21',
        '10.0.11.22',
        '10.0.11.23',
        '10.0.11.24',
        '10.0.11.25']
    ipRadius = 'pfSenseRadios.icea.ufop'

    with open('all_ruckus.txt', 'ab') as wfd:
        for f in ipsRuckus:
            try:
                with open(f, 'rb') as fd:
                    shutil.copyfileobj(fd, wfd)
            except OSError:
                continue
    with open('all_ubi.txt', 'ab') as wfd:
        for f in ipsUbi:
            try:
                with open(f, 'rb') as fd:
                    shutil.copyfileobj(fd, wfd)
            except OSError:
                continue
    with open('all_radius.txt', 'ab') as wfd:
        try:
            with open(ipRadius, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
        except OSError:
            pass
    with open('all_controladora_ruckos.txt', 'ab') as wfd:
        try:
            with open(ipControladora, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
        except OSError:
            pass

    importantVETsendMsg = sendMsg('all_ruckus.txt')
    importantVETinput = inputRuckos('all_ruckus.txt')
    importantVEThostapd = hostapd('all_ubi.txt')
    importantVETradius = leituraRadius('all_radius.txt')
    with open('dados_sendmsg_ruckos.csv', 'a') as f:
        for line in importantVETsendMsg:
            f.write(line)
    with open('dados_input_ruckos.csv', 'a') as f:
        for line in importantVETinput:
            f.write(line)
    #Ubi e Radius ainda não foram filtrados
    with open('dados_hostapd_ubi.csv', 'a') as f:
        for line in importantVEThostapd:
            f.write(line)
    with open('dados_radius.csv', 'a') as f:
        for line in importantVETradius:
            f.write(line)
