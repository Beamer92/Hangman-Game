import requests
import keys

def wordgen():
	#word = requests.get('http://setgetgo.com/randomword/get.php').text
	#print(word)
	ker = keys.api_key
	
	urlstring = "http://api.wordnik.com/v4/words.json/randomWords?minCorpusCount=10000&minDictionaryCount=20&excludePartOfSpeech=proper-noun,proper-noun-plural,proper-noun-posessive,suffix,family-name,idiom,affix&hasDictionaryDef=true&includePartOfSpeech=noun,verb,adjective,definite-article,conjunction&limit=26&maxLength=7&api_key=" 
	callstring = urlstring + ker
	request = requests.get(callstring)

	print(request)
wordgen()