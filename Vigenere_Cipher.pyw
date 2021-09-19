import PySimpleGUI as sg


def en_decrypt(input, key):
    ans_e = ''
    ans_d = ''
    key_u = ''

    if input == '' or key == '':
        return '', ''

    key_u = key*(len(input)//len(key)+1)

    for i, k in zip(input, key_u):
        if i >= 'a' and i <= 'z':
            ans_e_tmp = ord(i)+ord(k)-ord('a')
            ans_d_tmp = ord(i)+ord('a')-ord(k)

            if ans_e_tmp > ord('z'):
                ans_e_tmp -= 26
            if ans_d_tmp < ord('a'):
                ans_d_tmp += 26

            ans_e += chr(ans_e_tmp)
            ans_d += chr(ans_d_tmp)

        elif i >= 'A' and i <= 'Z':
            # ans_e_tmp = ord(i)+(ord('a')-ord('A'))+ord(k)-ord('a')
            k_Caps = ord(k)-(ord('a')-ord('A'))
            ans_e_tmp = ord(i)+k_Caps-ord('A')
            ans_d_tmp = ord(i)+ord('A')-k_Caps

            if ans_e_tmp > ord('Z'):
                ans_e_tmp -= 26
            if ans_d_tmp < ord('A'):
                ans_d_tmp += 26

            ans_e += chr(ans_e_tmp)
            ans_d += chr(ans_d_tmp)

        else:
            ans_e += i
            ans_d += i

    return ans_e, ans_d


sg.theme('DarkAmber')

layout = [
    [sg.Text('我們使用Vigenere Cipher (維吉妮亞密碼)。')],
    [sg.Text('只適用英文加密哦~(=^‥^)ノ')],
    [sg.Text('模式: '), sg.Radio('加密', 'mode', key='mode', default=True),
     sg.Radio('解密', 'mode')],
    [sg.Text('金鑰 (只能使用小寫英文字母): ')],
    [sg.InputText(size=(20, 1), key='key')],
    [sg.Text('訊息: ')],
    [sg.Multiline(size=(40, 3), key='message')],
    [sg.Text('訊息 (已加密): ', key='text_1')],
    [sg.Multiline(size=(40, 3), key='output')],
    [sg.OK('Convert')]
]

window = sg.Window('Vigenere Cipher', layout, font=("微軟正黑體", 18))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    ansE, ansD = en_decrypt(values['message'], values['key'])

    if values['mode'] == True:
        window['text_1'].update('訊息 (已加密): ')
        window['output'].update(ansE)
    else:
        window['text_1'].update('訊息 (已解密): ')
        window['output'].update(ansD)


window.close()
