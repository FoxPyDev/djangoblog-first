from django.shortcuts import render, redirect

posts = [
    {
        "Title": "dsadsadsa",
        "Description": "dsad hkjsah kdhakjh kjhkjsahkj hdj ka",
        "Author": "TestAdmin1",
        "Date": "1488",
     }
]


def indexpage(request):
    return render(request, 'index.html', {'articles': posts, "page": "index"})


def aboutpage(request):
    return render(request, 'about.html', {"page": "about"})

def contactpage(request):
    if request.method == "GET":
        return render(request, 'contact.html', {'articles': posts, "page": "index"})
    else:
        print(request.POST)
        with open('./contact_results.txt', 'a', encoding='utf-8') as file:
            file.writelines(f"Name: {request.POST['name']}, email: {request.POST['email']}, Subject: {request.POST['subject']}, Message: {request.POST['message']}")
        return redirect(contactpage)