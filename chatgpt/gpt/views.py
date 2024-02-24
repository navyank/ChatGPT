from django.shortcuts import render

# Create your views here.
import openai
openai.api_key="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"

# def chat_with_gpt(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role":"user","content":prompt}]
#     )
    
#     return response.choices[0].message.content.strip()
# if __name__=="__main__":
#     while True:
#         user_input = input("you: ")
#         if user_input.lower() in ["quit",'exit','bye']:
#             break
#         response =chat_with_gpt(user_input)
#         print("Chatbot: ",response)
def home(request):
    return render(request,"response.html")
def chat_with_gpt(request):
    chat_history = request.session.get('chat_history', [])
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = chat_with_gpt_api(user_input)
        chat_history.append(('User', user_input))
        chat_history.append(('Chatbot', response))
        request.session['chat_history'] = chat_history
        return render(request, 'response.html', {'user_input': user_input, 'response': response})
    return render(request, 'response.html')

def chat_with_gpt_api(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()
def chat_history(request):
    chat_history = request.session.get('chat_history', [])
    return render(request, 'chathistory.html', {'chat_history': chat_history})
def clear_history(request):
    # Clear chat history logic here (assuming chat history is stored in session)
    if 'chat_history' in request.session:
        del request.session['chat_history']
    return render(request,'chathistory.html')