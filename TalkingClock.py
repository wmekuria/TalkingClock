import winsound

time2word = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
}

def talkclock(time):
    hour, minute = time.split(":")

    if int(hour) < 12:
        period = 'am'
        #trick to support 00:00(24) time
        if int(hour) == 0:
            hour = '12'
    else:
        period = 'pm'
        if int(hour) == 12:
            hour = '12'
        else:
            hour = str(int(hour)-12)

# connect the time with the word
    hourstr = str(int(hour))
    hour = time2word[str(int(hour))]
    if int(minute) < 10:
        minute_pre = 'oh'
        # trick to support 00:00(24) time
        if int(minute) == 0:
            minute = '0'
            minute_pre = 'o`cklock'
        minute_pos = time2word[minute]
    elif 20 < int(minute) < 60:
        minute_pre = time2word[str((int(minute) / 10)*10)]
        minute_pos = time2word[str(int(minute) % 10)]
    else:
        minute_pre = ''
        minute_pos = time2word[minute]



    winsound.PlaySound('announcement.wav', winsound.SND_FILENAME) #'Hello as if a few seconds ago'
    winsound.PlaySound('its.wav', winsound.SND_FILENAME) #'It's'
    winsound.PlaySound(hourstr+'.wav', winsound.SND_FILENAME) #The hour

    # The minutes where a bit tricky. Didn't have the audio so I had to improvise..
    if 0 <= int(minute) <= 12:
        winsound.PlaySound(str(int(minute))+'.wav', winsound.SND_FILENAME)
    elif 13 <= int(minute) <= 19:
        winsound.PlaySound(str(int(minute)) + '.wav', winsound.SND_FILENAME)
        winsound.PlaySound('teen.wav', winsound.SND_FILENAME)
    elif 20 <= int(minute) <= 59:
        winsound.PlaySound(str((int(minute)/10)*10) + '.wav', winsound.SND_FILENAME)
        winsound.PlaySound('ty.wav', winsound.SND_FILENAME)
        winsound.PlaySound('ty'+str((int(minute)/10)%10)+'.wav', winsound.SND_FILENAME)


    winsound.PlaySound(period+'.wav', winsound.SND_FILENAME) #The period

    return "It's {0} {1} {2} {3}".format(hour, minute_pre, minute_pos, period)

if __name__ == '__main__':
    print talkclock(raw_input('Time: '))