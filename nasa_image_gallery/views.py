# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, "index.html")


# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.getAllImages()

    return images


# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].

    favourite_list = []
    images = getAllImagesAndFavouriteList(request)

    return render(
        request, "home.html", {"images": images, "favourite_list": favourite_list}
    )


# función utilizada en el buscador.
def search(request):
    search_msg = request.POST.get("query", None)
    if search_msg is not None and search_msg != "":

        # si se coloca una palabra en el buscador, se buscaran las imagenes en las que coincidan.
        images = services_nasa_image_gallery.getAllImages(input=search_msg)

    else:
        
        #caso contrario va a mostrar el buscador con el termino default (space)
        images = services_nasa_image_gallery.getAllImages()

    favourite_list = []
    return render(
        request, "home.html", {"images": images, "favourite_list": favourite_list}
    )



# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, "favourites.html", {"favourite_list": favourite_list})



@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request): #Al momento de querer salir del login utilizaremos esta funcion.
    pass
