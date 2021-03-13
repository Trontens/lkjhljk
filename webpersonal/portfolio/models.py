from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "titulo")
    description = models.TextField(verbose_name = "descripción")
    image = models.ImageField(verbose_name = "imagén", upload_to="projects")
    create = models.DateTimeField(auto_now_add= True,verbose_name = "Fecha de creación")
    update = models.DateTimeField(auto_now= True, verbose_name = "Fecha de última actualización")
    Referencia = models.URLField(max_length=200,null= True, blank=True)
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-create"]
    def __str__(self):
        return self.title


