a- settings/intalled_apps debemos incorporar el core creado por el proyecto

b- realizar las migraciones pendientes "python manage.py migrate"

c- al comienzo del proyecto la unica ruta que existe es /admin y es predeterminada

d- debemos crear un administrador por terminal

e- cuando se despliega un proyecto settings.py/debug debe estar en false

f- allowed-host debe ser "*" esto nos permitira trabajar con cualqueir host (es como cors)

g- creamos un archivo view.py e incorporamos from django.views.generic import view


h- vamos a crear una clase que llame a un metodo get() que tendra un return render(request, 'template o html', context)

i- en settings verificaremos que el template pueda ser encontrado: os.path.join() con un import os

j- para crear una nueva app "python manage.py startapp blog"
