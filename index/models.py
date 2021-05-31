from django.db import models

# Create your models here.

class SaleFutures(models.Model):
        # informations
    title = models.CharField('Title', max_length=250, db_index=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sale_futures'
        verbose_name = 'Sale_futures'
        verbose_name_plural = 'Sale_futures'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 


class Logo(models.Model):

    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Logo', upload_to='logo')
    

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'logo'
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


class Banner(models.Model):
    # informations
    title = models.CharField('Title', max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField('Link', max_length=300, blank=True, null=True)
    image = models.ImageField('Image', upload_to='banner_pics', null=True, blank=True)
    is_main = models.BooleanField('Main Image', default=False)
    is_second_yuxari = models.BooleanField('Second yuxari', default=False)
    is_second_ashagi = models.BooleanField('Second asagi', default=False)
    is_third_sol = models.BooleanField('Third sol', default=False)
    is_third_sag = models.BooleanField('Third sag', default=False)
    is_third_orta = models.BooleanField('Third orta', default=False)
    # is_full_screen = models.BooleanField('Full Screen', default=False)
    # video = models.CharField('Title', max_length=100, db_index=True, null=True, blank=True)
     
    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banner'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ParallaxBanner(models.Model):
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    description1 = models.CharField(max_length=255, blank=True)
    description2 = models.CharField(max_length=255, blank=True)
    image = models.ImageField('Slide Imahe', upload_to='slide_image', null=True, blank=True)
    # is_main = models.BooleanField('Main Slider', default=False)
    # is_full_screen = models.BooleanField('Full Screen', default=False)
    # video = models.CharField('Title', max_length=100, db_index=True, null=True, blank=True)
     
    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'parallax_banner'
        verbose_name = 'parallax_banner'
        verbose_name_plural = 'parallax_banners'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


class Subscriber(models.Model):
    email = models.CharField('Email', max_length=40)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ('-created_at',)

    def __str__(self):
        return self.email 
