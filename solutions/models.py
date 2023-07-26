from django.db import models
from django.utils.translation import gettext_lazy as _


class Platforms(models.Model):
    pass
    # turnkey_solutions = models.IntegerField()

class Solutions(models.Model):
    name_solution = models.CharField(max_length=255)
    business_model = models.CharField(max_length=255)
    business_area = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    type_solution = models.CharField(max_length=255)
    short_description = models.TextField()
    messengers = models.CharField(max_length=255)
    integration_crm = models.CharField(max_length=255)
    integration_payment_services = models.CharField(max_length=255)
    tasks = models.TextField()
    platform = models.ForeignKey(Platforms,
                                  on_delete=models.CASCADE,
                                  #to_field='turnkey_solutions', 
                                  related_name='solutions',
                                  )
    image = models.FileField(null=True, blank=True) #upload
    activities_to_complete_tasks = models.TextField()
    full_description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Работа с решениями"

    def __str__(self):
        return self.name_solution


class Solution_filters(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    properties = models.JSONField(null=True, blank=True)


class Filter_solutions(models.Model):
    solution = models.ForeignKey(Solutions,
                                  on_delete=models.CASCADE, 
                                  related_name='filter_solutions'
                                  )
    filter_solution = models.ForeignKey(Solution_filters, 
                                        on_delete=models.CASCADE, 
                                        related_name='filter_solutions'
                                        )
                                                             

                                                            


    
