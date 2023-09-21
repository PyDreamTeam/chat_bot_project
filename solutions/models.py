from django.db import models


class SolutionGroup(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=800, null=True)

    def __str__(self):
        return f"{self.title},"


class SolutionFilter(models.Model):
    title = models.CharField(max_length=100)
    functionality = models.CharField(max_length=200, null=True)
    integration = models.CharField(max_length=800, null=True)
    multiple = models.BooleanField(default=True)
    group = models.ForeignKey(SolutionGroup, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=800, null=True)

    def __str__(self):
        return f"{self.title}, {self.group}"


class SolutionTag(models.Model):
    title = models.ForeignKey(SolutionFilter, on_delete=models.CASCADE)
    properties = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    image = models.CharField(max_length=800, null=True)
    is_message = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.properties}"


BUY_SOLUTION = (
    ("Buy this turnkey solution", "Buy this turnkey solution"),
    ("Buy this ready-made with the possibility of refinement", "Buy this ready-made with the possibility of refinement"),
)


class Solution(models.Model):
    title = models.CharField(max_length=100)
    business_model = models.CharField(max_length=200)
    business_area = models.CharField(max_length=100)
    business_niche = models.CharField(max_length=100)
    objective = models.CharField(max_length=100)
    solution_type = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    platform = models.CharField(max_length=100)
    messengers = models.CharField(max_length=100)
    integration_with_CRM = models.CharField(max_length=100)
    integration_with_payment_systems = models.CharField(max_length=100)
    tasks = models.CharField(max_length=100)
    actions_to_complete_tasks = models.CharField(max_length=100)
    image = models.URLField()
    number = models.CharField(max_length=200, choices=BUY_SOLUTION)
    filter = models.ManyToManyField(SolutionTag)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    advantages = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    full_description = models.CharField(max_length=300)
    dignity = models.CharField(max_length=300)
    steps_title = models.CharField(max_length=100)
    steps_text = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}, {self.short_description}"


