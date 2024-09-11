from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'company' : 'Toko Sinar Abadi',
        'owner_name': 'Ida Made Revindra Dikta Mahendra',
        'owner_class': 'kelas PBP C'
    }

    return render(request, "main.html", context)