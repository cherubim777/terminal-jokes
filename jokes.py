from pyfiglet import figlet_format as pformat
from termcolor import colored as colorize
import requests

text = pformat("BIG  SMILE !")
text = colorize(text, 'magenta', on_color='on_yellow', attrs=['bold', 'blink'])

print(text)
joke_topic = input('let me tell a joke! Give me a topic: ')

url = 'https://icanhazdadjoke.com/search'

response = requests.get(
	url,
	headers = {"Accept": "application/json"},
	params = {'term': joke_topic }).json()

jokes = [i['joke'] for i in response['results']]

print(f"I found you {response['total_jokes']} jokes on {joke_topic}. Here is one")


for i in jokes:
	print(colorize(i, 'yellow', attrs=['bold']))
	jokes.remove(i)
	x = input('do you want another one (y/n): ')
	if x in ['yes', 'y', 'Y', 'Yes', 'YES']:
		if len(jokes) == 0:
			print(colorize(f'Oops, ther is no another joke on {joke_topic}', 'red'))
			break
		continue
	else:
		break
