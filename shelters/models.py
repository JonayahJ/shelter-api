from django.db import models

# Dictionaries
TYPE_OF_SHELTER = [
    ("General", "General Shelter"),
    ("Gender/Age Restrictions", "Gender and Age Restrictions"),
    ("Men's", "Men's Shelters"),
    ("Women's", "Women's Shelters"),
    ("Women and Kids", "Women's and Children's Shelters"),
    ("Teens", "Teenage Shelters"),
    ("Seniors", "Senior Citizens Shelters"),
    ("Families", "Family Shelters"),
    ("Long-Term", "Transitional Emergency Long-Term Supportive Housing"),
    ("Emergency", "Emergency Shelter"),
]

SHELTER_SERVICES = [
    ("Domestic Violence Care", "Domestic Violence Care"),
    ("Case Mgmt", "Case Management or Counseling Faith/Religion-Based Help"),
    ("Veterans", "Veteran Services"),
    ("Medical", "Medical services"),
    ("Mental Health", "Mental health care"),
    ("Addiction", "Addiction Care"),
    ("Legal", "Legal assistance"),
]

# Shelter Model
class Shelter(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=12)
    telephone = models.CharField(max_length=12)
    type_of_shelter = models.CharField(max_length=50, choices=TYPE_OF_SHELTER, default="General Shelter")
    shelter_services = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name