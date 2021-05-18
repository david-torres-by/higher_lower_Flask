from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def guess_the_number():
	return '<h1 >Guess a number between 0 and 9!</h1>' \
		   '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif width="500">'

@app.route('/<int:number_guessed>')
def guess(number_guessed):
	if random_number == number_guessed:
		return f'<h1 styling = "color:blue">"You have guessed {number_guessed}, that is correct!"</h1>' \
			   '<img src=https://media4.giphy.com/media/FbyqoWvEHmV9K/giphy.gif?cid=ecf05e478kef73a10vjy09tcprcbvkarcuz4uatuz839az1k&rid=giphy.gif&ct=g width="500">'
	elif number_guessed > random_number:
		return f'<h1 styling = "color:red">"Way too big"</h1>' \
			   '<img src=https://media1.giphy.com/media/3oEdv898CETgzT5vxu/giphy.gif?cid=ecf05e47mg17t73sh0nav4ijs19m3g2d7ifpu6lhf3cvl4gg&rid=giphy.gif&ct=g width="500">'
	elif number_guessed < random_number:
		return f'<h1 styling = "color:red">"Way too small"</h1>' \
			   '<img src=https://media4.giphy.com/media/E9uxGrsyXjnSU/giphy.gif?cid=ecf05e4785vjdwcx35hht1rorhzzbliw6dwz2vdrk53mb222&rid=giphy.gif&ct=g width="500">'

if __name__ == '__main__':
	app.run(debug=True)