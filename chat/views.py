from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import re
import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_WEATHER = "As an AI Bot I can't tell you present condition !"
R_CHEAPEST = "Oppo A57 - 5.2 HD Display - 4GB RAM - 64GB ROM"
R_EXPENSIVE = "Apple 14 pro max 128gb box pack"
R_THANK = "You are welcome ! "
R_DEVELOPED = "Mr.Arslan Javed developed me"
R_BEST_APPLE = " Best Apple phone is Apple 14 pro max 128gb box pack"
R_BEST_XIAOMI="Best Xiamo phone is Xiaomi Redmi Note 12 Pro RAM 8 GB ROM "
R_BEST_SAMSUNG="Samsung Galaxy A54 RAM 8 GB ROM 256 GB"
R_BEST_ITEL="itel S23  HD+ Display | Up to 16+256GB Storage with  50 MP AI Camera"
R_BEST_VIVO="Vivo V29 12GB Ram 256GB Rom 6.78 Inches AMOLED Display , 4600 mAh "
R_BEST_TECNO="Tecno Camon 20 , 8GB RAM 256GB ROM , 64MP Main Camera , Fingerprint , 5000mAh Fast Charging"
R_BEST_INFINIX="Infinix Zero 30 4G RAM 8 GB ROM 256 GB Front Camera 50 MP"
R_UNDER_30000="Redmi A2 , Redmi 12C , itel A60s , Infinix Smart 7 , Sparx Neo X ,Oppo A57 ,Vivo Y85,Redmi A1 Plus,Nokia C31 "
R_UNDER_45000="Realme Narzo 50 A , Redmi A2 plus , infinix hot 30 , Itel S 23 , Infinix smart 7 ,Oppo A57 ,Vivo Y85,Nokia C31 "
R_ABOVE_45000="Iphone X, Redmi Note 12, infinix note 30 pro , Samsung Galaxy A04 S, Iphone SE 2nd Generation,Samsung Galaxy A24 S,Iphone 14pro max"
R_ABOVE_30000="Realme Narzo 50 A , Redmi A2 plus , infinix hot 30 , Itel S 23 , Infinix smart 7 ,Oppo A57 ,Vivo Y85,Nokia C31 "
R_PHONE_4=" Redmi Note 12, Redmi Note 12 pro, Samsung galaxy A04 S  , Sparks S3,Samsung galaxy A33,RedMi Note 12 S"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Ummmm.",
                "What does that mean?"][
        random.randrange(4)]
    return response


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


@csrf_exempt

def bot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        response_text = check_all_messages(split_message)
        return render(request, 'chatbot.html', {'response_text': response_text})
    else:
        # Handle GET requests
        return render(request, 'chatbot.html', {'response_text': 'Please make a POST request with user input.'})


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response,
                                                               required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Mr.Arslan Javed', ['who', 'is', 'your', 'developer'], required_words=['your', 'developer'])
    response('Rs.267,000', ['price', 'expensive', 'phone'], required_words=['price', 'expensive', 'phone'])
    response('Rs.13,999', ['price', 'cheapest', 'phone'], required_words=['price', 'cheapest', 'phone'])
    #---------------------------------------------------------------------------------------------------------
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(R_WEATHER, ['hows', 'weather'], required_words=['weather'])
    response(R_CHEAPEST, ['cheapest', 'phone'], required_words=['cheapest', 'phone'])
    response(R_EXPENSIVE, ['expensive', 'phone'], required_words=['expensive', 'phone'])
    response(R_THANK, ['thank', 'you'], required_words=['thank', 'you'])
    response(R_DEVELOPED, ['who', 'developed', 'you'], required_words=['who', 'developed', 'you'])
    response(R_BEST_APPLE, ['best', 'apple', 'phone'], required_words=['best', 'apple', 'phone'])
    response(R_BEST_XIAOMI, ['best', 'xiaomi', 'phone'], required_words=['best', 'xiaomi', 'phone'])
    response(R_BEST_SAMSUNG, ['best', 'samsung', 'phone'], required_words=['best', 'samsung', 'phone'])
    response(R_BEST_ITEL, ['best', 'itel', 'phone'], required_words=['best', 'itel', 'phone'])
    response(R_BEST_VIVO, ['best', 'vivo', 'phone'], required_words=['best', 'vivo', 'phone'])
    response(R_BEST_TECNO, ['best', 'tecno', 'phone'], required_words=['best', 'tecno', 'phone'])
    response(R_BEST_INFINIX, ['best', 'infinix', 'phone'], required_words=['best', 'infinix', 'phone'])
    response(R_UNDER_30000,["phone","under","30000"],required_words=["phone","under","30000"])
    response(R_UNDER_45000,["phone","under","45000"],required_words=["phone","under","45000"])
    response(R_ABOVE_45000,["phone","above","45000"],required_words=["phone","above","45000"])
    response(R_ABOVE_30000,["phone","above","30000"],required_words=["phone","above","30000"])
    response(R_PHONE_4,["phone","4","rating"],required_words=["phone","4","rating"])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match
