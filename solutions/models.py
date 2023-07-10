from django.db import models


class Platforms(models.Model):
    pass
    # turnkey_solutions = models.IntegerField()

class Solutions(models.Model):
    platform = models.ForeignKey(Platforms,
                                  on_delete=models.CASCADE,
                                  #to_field='turnkey_solutions', 
                                  related_name='solutions',
                                  )
    image = models.ImageField(null=True, blank=True) #upload
    short_description = models.CharField(max_length=250, null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


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
                                                             

                                                            


    
