import twitter
import string
api = twitter.Api()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)

class Search():
	def render(self, pixels):
		i = 0
		searchresult = api.GetSearch("blue OR orange OR yellow OR green OR purple OR red")
		for s in searchresult:
			print s.text
			i = i+1
			if (s.text.find("orange") > -1):
				print("orange")
				pixels[i] = orange
			elif (s.text.find("blue") > -1):
				print("blue")
				pixels[i] = blue
			elif (s.text.find("yellow") > -1):
				print("yellow")
				pixels[i] = yellow
			elif (s.text.find("green") > -1):
				print("green")
				pixels[i] = green
			elif (s.text.find("purple") > -1):
				print("purple")
				pixels[i] = purple
			elif (s.text.find("red") > -1):
				print("red")
				pixels[i] = red
			if( i > 6):
				i = 0

if __name__ == "__main__":
	import octoapi
	pixels = [(),(),(),(),(),(),(),()]
	s = Search()
	s.render(pixels)
	octoapi.write(pixels)
