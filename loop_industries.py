industries = ['industry=10', '&industry=11', 'industry=12', 'industry=13',
              'industry=14', 'industry=15', 'industry=17', 'industry=18',
              'industry=19', 'industry=21', 'industry=23', 'industry=24',
              'industry=25', 'industry=26', 'industry=27', 'industry=28',
              'industry=29', 'industry=30']

scrap = "islamkamran&region=US"
scrap = scrap+industries[1]
print(scrap)

scrap = scrap.split(industries[1])[0]
print(scrap)


# brand_industry = models.BigIntegerField(unique=True)
# brand_name = models.CharField(max_length=255)
# brand_landing_page = models.URLField(null=True)

