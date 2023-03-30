from django.shortcuts import render

def home(request):
	# reauest это параметре, содержащий в себе очень много инфы.
	return render(request, 'home.html', {'greeting':'Hello!'})

def reverse(request):
	# reauest это параметре, содержащий в себе очень много инфы.
	user_text = request.GET['usertext']
	#print(user_text) #такой текст выводится в терминале
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':user_text[::-1], 'num_of_words':len(user_text.split())}) #теперь в файле reverse.html мы можешь обращаться к ключу 'usertext'	