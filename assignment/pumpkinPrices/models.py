from django.db import models

Atlanta = "ATLANTA"
Baltimore = "BALTIMORE"
Boston = "BOSTON"
Chicago = "CHICAGO"
Columbia = "COLUMBIA"
Dallas = "DALLAS"
Detroit = "DETROIT"
Los_Angeles = "LOS ANGELES"
Miami = "MIAMI"
New_York = "NEW YORK"
Philadelphia = "PHILADELPHIA"
San_Fransisco = "SAN FRANSISCO"
St_Louis = "ST. LOUIS"
city_choice = [
	(Atlanta,'ATLANTA'),
	(Baltimore,'BALTIMORE'),
	(Boston,'BOSTON'),
	(Chicago,'CHICAGO'),
	(Columbia,'COLUMBIA'),
	(Dallas,'DALLAS'),
	(Detroit,'DETROIT'),
	(Los_Angeles,'LOS ANGELES'),
	(Miami,'MIAMI'),
	(New_York,'NEW YORK'),
	(Philadelphia,'PHILADELPHIA'),
	(San_Fransisco,'SAN FRANSISCO'),
	(St_Louis,'ST. LOUIS'),														
]

HOWDEN_TYPE = "HOWDEN TYPE"
PIE_TYPE = "PIE TYPE"
MINIATURE = "MINIATURE"
HOWDEN_WHITE_TYPE = "HOWDEN WHITE TYPE"
CINDERELLA = "CINDERELLA"
FAIRY_TALE = "FAIRY TALE"
BIG_MACK_TYPE = "BIG MACK TYPE"
MIXED_HEIRLOOM_VARIETIES = "MIXED HEIRLOOM VARIETIES"
BLUE_TYPE = "BLUE TYPE"
KNUCKLE_HEAD = "KNUCKLE HEAD"

variety_choice = [
	(HOWDEN_TYPE, "HOWDEN TYPE"),
	(PIE_TYPE, "PIE TYPE"),
	(MINIATURE, "MINIATURE"),
	(HOWDEN_WHITE_TYPE, "HOWDEN WHITE TYPE"),
	(CINDERELLA, "CINDERELLA"),
	(FAIRY_TALE, "FAIRY TALE"),
	(BIG_MACK_TYPE, "BIG MACK TYPE"),
	(MIXED_HEIRLOOM_VARIETIES, "MIXED HEIRLOOM VARIETIES"),
	(BLUE_TYPE, "BLUE TYPE"),
	(KNUCKLE_HEAD, "KNUCKLE HEAD"),
]
class Pumpkin(models.Model):
	
	city = models.CharField(max_length = 100, choices = city_choice, default = Atlanta)
	variety = models.CharField(max_length = 100, choices = variety_choice, default = HOWDEN_TYPE)
	date = models.DateField()
	low_price = models.DecimalField(max_digits = 6, decimal_places = 3)
	high_price = models.DecimalField(max_digits = 6, decimal_places = 3)

	class Meta:
		ordering = ('city',)

	def __str__(self):
		return("City:{} Variety:{} Date:{}".format(self.city, self.variety, self.date))	
# Create your models here.
