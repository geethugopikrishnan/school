from .models import Department, Course


def menu_links(request):
    links = Department.objects.all()
    return dict(links = links)


