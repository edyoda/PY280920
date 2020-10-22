def microsoft(work_given_to_microsoft):
	ceo = 'satya nadela'
	document = [ceo,work_given_to_microsoft]
	# print(locals())
	print(globals())
	return document

def netflix(movie_you_want_to_watch):
	return "played+netflix&chill with the movie"+movie_you_want_to_watch

# print("value os __name__ is ",__name__)

if __name__=="__main__":
	print(netflix("PhirHeraPheri"))
