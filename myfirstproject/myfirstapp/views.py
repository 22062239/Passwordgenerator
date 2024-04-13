from django.shortcuts import render
import string
import random

# Create your views here.
def home(request):
    return render(request, 'myfirstapp/home.html')

def generate_password(request):
    if request.method == 'POST':
        passlength = int(request.POST['passlength'])
        choices = request.POST.getlist('choice')  # Use getlist to retrieve multiple values
        characterList = ""
        
        for choice in choices:
            if choice == '1':
                characterList += string.digits
            elif choice == '2':
                characterList += string.ascii_letters
            elif choice == '3':
                characterList += string.punctuation
        
        password = []
        for i in range(passlength):
            if characterList == "":
                break
            else:
                randomchar = random.choice(characterList)
            password.append(randomchar)

        if characterList == "":
            result = "Could not generate password"
        else:
            result = "".join(password)

        return render(request, 'myfirstapp/result.html', {'result': result})

