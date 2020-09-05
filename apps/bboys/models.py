from django.db import models

class Crew(models.Model):

    name = models.CharField( max_length=50)

    class Meta:
        verbose_name = ("Crew")
        verbose_name_plural = ("Crews")

    def __str__(self):
        return self.name

class City(models.Model):

    city_name = models.CharField( max_length=50 )

    class Meta:
        verbose_name = ("Ciudad")
        verbose_name_plural = ("Ciudades")

    def __str__(self):
        return self.city_name


class Bboy(models.Model):

    name = models.CharField( max_length=50 )
    phone = models.CharField( max_length=50)
    email = models.EmailField(max_length=254, null = True, blank = True)
    dj = models.BooleanField()
    judge = models.BooleanField()
    points = models.IntegerField()
    crew = models.ForeignKey(Crew, null= True, blank= True, related_name='crew', on_delete=models.CASCADE)
    city = models.ForeignKey(City, null = True, blank = True, related_name = 'city', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Bboy")
        verbose_name_plural = ("Bboys")

    def __str__(self):
        return self.name
