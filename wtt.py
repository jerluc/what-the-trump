from urllib import urlopen
import json
import subprocess


def dictate_quote():
    res = urlopen('https://api.whatdoestrumpthink.com/api/v1/quotes/random')
    res_dict = json.load(res)
    subprocess.call(['say', res_dict['message']])


def main():
    while True:
        choice = raw_input('Would you like to hear Donald Trump? ')
        if choice == 'why yes':
            dictate_quote()
        else:
            print('Yeah, me neither')
            break


if __name__ == '__main__':
    main()
