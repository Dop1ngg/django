from django.shortcuts import render


def index(request):
    context = {
        'title': "Home - главная",
        'content': "Магазин мебели HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': "Home - О нас",
        'content': "О нас",
        'text_on_page': """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Aenean risus metus, pellentesque a lorem et, aliquet accumsan ligula.
                            Praesent consectetur nibh eros, at dapibus odio fermentum nec. Sed in ultrices elit.
                            Morbi sem ante, tincidunt non arcu sit amet, fringilla tincidunt urna.
                            In ante massa, bibendum suscipit lectus at, aliquet rutrum dolor."""
    }

    return render(request, 'main/about.html', context)
