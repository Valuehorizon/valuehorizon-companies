# Import Django libraries
from django.db import models
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator

# Import Valuehorizon libraries
from countries.models import Country
from people.models import Person

# Import other libraries
import calendar as cal
from datetime import date, datetime
from decimal import Decimal

class Sector(models.Model):
    """
    Used for industry information.
    Represents the GICS classification system.
    """

    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=2, unique=True)
    description = models.TextField(blank=True)
    custom = models.BooleanField(default=False, help_text="True if created by user (or otherwise customized)")

    class Meta:
        verbose_name_plural = 'GICS 1 Sectors'
        verbose_name = 'GICS 1 Sector'
        ordering = ['symbol', 'name', ]
        
    def __unicode__(self):
        return u'%s (%s)' % (unicode(self.name), unicode(self.symbol) )
    
    
    
        
        
class IndustryGroup(models.Model):
    """
    Used for industry information. Represents the GICS
    classification system.
    """

    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=4, unique=True)
    description = models.TextField(blank=True)
    sector = models.ForeignKey(Sector)
    custom = models.BooleanField(default=False, help_text="True if created by user (or otherwise customized)")

    class Meta:
        verbose_name_plural = 'GICS 2 Industry Groups'
        verbose_name = 'GICS 2 Industry Group'
        ordering = ['symbol', 'name', ]
        
    def __unicode__(self):
        return u'%s (%s)' % (unicode(self.name), unicode(self.symbol) )
    
    
        
    
class Industry(models.Model):
    """
    Used for industry information. Represents the GICS
    classification system.
    """

    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=6, unique=True)
    description = models.TextField(blank=True)
    industry_group = models.ForeignKey(IndustryGroup)
    sector = models.ForeignKey(Sector)
    custom = models.BooleanField(default=False, help_text="True if created by user (or otherwise customized)")
    
    class Meta:
        verbose_name_plural = 'GICS 3 Industry'
        verbose_name = 'GICS 3 Industry'
        ordering = ['symbol', 'name', ]
        
    def __unicode__(self):
        return u'%s (%s)' % (unicode(self.name), unicode(self.symbol) )
    
        
    
class SubIndustry(models.Model):
    """
    Used for industry information. Represents the GICS
    classification system.
    """

    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=8, unique=True)
    description = models.TextField(blank=True)
    industry = models.ForeignKey(Industry)
    custom = models.BooleanField(default=False, help_text="True if created by user (or otherwise customized)")

    class Meta:
        verbose_name_plural = 'GICS 4 Sub-Industry'
        verbose_name = 'GICS 4 Sub-Industry'
        ordering = ['symbol', 'name', ]
        
    def __unicode__(self):
        return u'%s (%s)' % (unicode(self.name), unicode(self.symbol) )



    
class Company(models.Model):
    """
    Represents a company.
    """
    
    COMPANY_CHOICES = (
        (u'LTD', u'Limited Liability'),
        (u'P',   u'Partnership'),
        (u'SP',  u'Sole Proprietorship'),
        (u'NV',  u'Naamloze vennootschap'),
    )
    company_type = models.CharField(max_length=255, choices=COMPANY_CHOICES)
    
    STATUS_CHOICES = (
        (u'A', u'Active (Going Concern)'),
        (u'N', u'Active (Non-Going Concern)'),
        (u'D', u'Active (Developmental)'),
        (u'I', u'Inactive'),
        (u'U', u'Unknown'),
    )
    status_type = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    # Company Details
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=15, blank=True, null=True, help_text="eg. Freddie Mac")
    include_article_in_description = models.BooleanField(default=False, help_text="eg. [the] National Biscuit Company")
    slug_name = models.CharField(max_length=255, unique=True)  # To do: change to slugfield
    address = models.TextField(blank=True)
    country = models.ForeignKey(Country, help_text="Country in which the company is registered" )
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True, validators=[MaxLengthValidator(370)])
    phone = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    website_url = models.URLField(blank=True)
    
    # Dates
    registration_date = models.DateField(null=True, blank=True, help_text="Date founded")
    latest_incorporation_date = models.DateField(null=True, blank=True, help_text="Incorporation date of latest incarnation")
    
    # Cache sectors
    sub_industry = models.ForeignKey(SubIndustry)
    industry = models.ForeignKey(Industry, blank=True, null=True, editable=False)
    industry_group = models.ForeignKey(IndustryGroup, blank=True, null=True, editable=False)
    sector = models.ForeignKey(Sector, blank=True, null=True, editable=False)
    
    # Cache sector names
    sub_industry_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    industry_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    industry_group_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    sector_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    
    # Financial Statements
    financial_year_end = models.DateField(null=True, blank=True)
    FP_CHOICES = (
        (u'A', u'Annual'),
        (u'S', u'Semi-Annual'),
        (u'Q', u'Quarterly'),
        (u'U', u'Unknown'),
    )
    financial_publication_frequency = models.CharField(max_length=1, choices=FP_CHOICES, default="U", help_text='How often does this company produce financial statements?')    

    # Special company flags
    is_auditor = models.BooleanField(default = False, help_text='Is this company an Auditor, eg. PwC, Deloitte, etc.?.')
    is_credit_rating_agency = models.BooleanField(default = False, help_text='is this company a credit rating agency, eg. S&P, Fitch, etc.')
    is_government_agency = models.BooleanField(default = False, help_text='Is this company a govermenet agency?')
    is_non_profit = models.BooleanField(default = False, help_text='Is this a non-profit company?')
    is_government = models.BooleanField(default = False, help_text='Is this a government?')
    is_fund = models.BooleanField(default = False, help_text='Is this a Mutual Fund?')
    
    class Meta:
        verbose_name_plural = 'Companies'
        verbose_name = 'Company'
        ordering = ['name', ]
        unique_together = ("name", "country")

    def __unicode__(self):
        return u'%s' % (unicode(self.name),)# ' ID: ' + unicode(self.id))
    
    def get_absolute_url(self):
        if not self.is_government and self.primary_stock_url != None:
            return self.primary_stock_url
        else:
            return None
    	
	
    
  
    def get_all_children(self, include_self=False):
        """
        Return all subsidiaries of this company.
        """
        ownership = Ownership.objects.filter(parent=self)
        subsidiaries = Company.objects.filter(child__in=ownership)
        for sub in subsidiaries:
            subsidiaries = subsidiaries | sub.get_all_children()
	
	if include_self == True:
	    self_company = Company.objects.filter(id=self.id)
	    subsidiaries = subsidiaries | self_company
        return subsidiaries
    
    def get_all_parents(self):
        """
        Return all parents of this company.
        """
        ownership = Ownership.objects.filter(child=self)
        parents = Company.objects.filter(parent__in=ownership)
        for parent in parents:
            parents = parents | parent.get_all_parents()
        return parents
    
    def get_all_related_companies(self, include_self=False):
            """
            Return all parents and subsidiaries of the company
            Include the company if include_self = True
            """
            parents = self.get_all_parents()
            subsidiaries = self.get_all_children()
            related_companies = parents | subsidiaries
            
            if include_self == True:
                company_qs = Company.objects.filter(id=self.id)
                related_companies = related_companies | company_qs
	    
	    related_companies_ids = [ company.id for company in list(set(related_companies))]
	    related_companies = Company.objects.filter(id__in=related_companies_ids)
            return related_companies
    
    def get_immediate_children(self):
        """
        Return all direct subsidiaries of this company. 
        Excludes subsidiaries of subsidiaries
        """
        ownership = Ownership.objects.filter(parent=self)
        subsidiaries = Company.objects.filter(child__in=ownership).distinct()
        return subsidiaries
    
    def get_immediate_children_ownership(self):
        """
        Return all direct subsidiaries of this company AS OWNERSHIP OBJECTS. 
        Excludes subsidiaries of subsidiaries.
        
        """
        ownership = Ownership.objects.filter(parent=self).select_related('child', 'child__country')
        return ownership
    
    def get_immediate_parents(self):
        """
        Return all direct parents of this company. Excludes parents of parents
        """
        ownership = Ownership.objects.filter(child=self)
        parents = Company.objects.filter(parent__in=ownership).distinct()
        return parents
    
    def get_directors(self):
        """
        Return all directors for this company
        """
        directors = Director.objects.filter(company=self, is_current=True).select_related('person')
        return directors
    
    def get_stocks(self):
        """
        Return all stocks for this company
        """
        stocks = Stock.objects.filter(company=self)
        return stocks
    
    def get_latest_annual_financials(self):
        """
        Returns the latest annual financial statement model.
        """
        try:
            statement = FinancialStatement.objects.filter(company=self, statement_type="A").latest()
        except FinancialStatement.DoesNotExist:
            statement = None
        return statement
    
    def get_latest_financials(self):
        """
        Returns the latest financial statement model (interim or annual).
        """
        try:
            statement = FinancialStatement.objects.filter(company=self).latest()
        except FinancialStatement.DoesNotExist:
            statement = None
        return statement
    

    
    def cache_data(self):
        """
        Cache some basic data such as financial statement metrics
        """
        


        # Set Slug if not set
        if not self.slug_name:
            self.slug_name=slugify(self.name).strip()
            if len(self.slug_name) > 255:
                self.slug_name = self.slug_name[0:254]            
    
    def get_name_on_date(self, date):
	"""
	Get the name of a company on a given date. Accounts for
	name changes that may have occurred.
	"""
	if date == None:
	    return self.name
	
	post_name_changes = CompanyNameChange.objects.filter(company=self,
                                                             date__gte=date).order_by('date')
	if post_name_changes.count() == 0:
	    return self.name
	else:
	    return post_name_changes[0].name_before    

    def save(self, *args, **kwargs):
        """
        This method autogenerates the auto_generated_description field
        """
        
        # Cache basic data
        self.cache_data()
	
	if str(self.trade_name).strip() == "":
	    self.trade_name = None
	
	# Short description check
	if len(str(self.short_description)) > 370:
	    raise AssertionError("Short description must be no more than 370 characters")
        
        
        if self.sub_industry != None:
            # Cache GICS
            self.industry = self.sub_industry.industry
            self.industry_group = self.sub_industry.industry.industry_group
            self.sector = self.sub_industry.industry.industry_group.sector
            # Cache GICS names
            self.sub_industry_name = self.sub_industry.name
            self.industry_name = self.industry.name
            self.industry_group_name = self.industry_group.name
            self.sector_name = self.sector.name
        

        
        # Call save method
        super(Company, self).save(*args, **kwargs) # Call the "real" save() method.
        
    
class CompanyNameChange(models.Model):
    """
    Represents a company name change
    """
    
    date = models.DateField()
    name_before = models.CharField(max_length=255)
    name_after = models.CharField(max_length=255)
    
    short_description = models.CharField(max_length=85)
    long_description = models.CharField(max_length=255)
    company = models.ForeignKey(Company)
    
    STATUS_CHOICES = (
    ("CO",    u'Completed'),
    ("FA",    u'Failed'),
    ("UP",    u'Upcoming'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="CO")    
    
    class Meta:
	verbose_name_plural = 'Company Name Changes'
	verbose_name = 'Company Name Change'
	ordering = ['date']
	unique_together = ("company", 'date')

    def __unicode__(self):
	return u'%s, %s' % (unicode(self.company),
                            unicode(self.date))
    

class Ownership(models.Model):
    """
    Represents an ownership mapping of a company. That is, this class maps a parent/owner
    to a subsidiary.
    """
    
    name = models.CharField(max_length=255, blank=True, null=True, editable=False)  # This will speed up the admin
    parent = models.ForeignKey(Company, related_name='parent')
    child = models.ForeignKey(Company, related_name='child')
    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    OWNERSHIP_TYPE = (
        (u'SUB', u'Subsidiary'),
        (u'ASS', u'Associate'),
        (u'JV',  u'Joint Venture'),
        (u'I',   u'Institutional'),
    )
    ownership_type = models.CharField(max_length=3, choices=OWNERSHIP_TYPE)
    
    class Meta:
	verbose_name_plural = 'Ownership'
	verbose_name = 'Ownership'
	ordering = ['parent', 'child' ]
	unique_together = ("parent", "child")
	
    def __unicode__(self):
	return u'%s - (%s%%)' % (unicode(self.name), unicode(self.amount))
    
    def save(self, *args, **kwargs):
	"""
	Generate a name, and ensure amount is less than or equal to 100
	"""
	
	self.name = str(self.parent.name) + "   -   " + str(self.child.name) + "  -  " + str(self.ownership_type) 

	if self.amount > 100:
	    raise IntegrityError("Ownership amount cannot be more than 100%")
	elif self.amount < 0:
	    raise IntegrityError("Ownership amount cannot be less than 0%")
	else:
	    super(Ownership, self).save(*args, **kwargs) # Call the "real" save() method.
    




class Director(models.Model):
    """
    Represents each member of a company's board of directors.
    """

    name = models.CharField(max_length=255, blank=True, null=True)  # This will speed up the admin
    company = models.ForeignKey(Company)
    person = models.ForeignKey(Person)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=True)
    position = models.CharField(max_length=255, blank=True)

    class Meta:
	verbose_name_plural = 'Directors'
	verbose_name = 'Director'
	ordering = ['is_current', 'company', 'person', ]
	unique_together = ("company", "person", "start_date", "end_date")


    def __unicode__(self):
	return u'%s' % (unicode(self.name))
    
    def tenure(self):
	"""
	Calculates board tenure in years
	"""
	if self.end_date:
	    return round((date.end_date - self.start_date).days / 365., 2)
	else:
	    return round((date.today() - self.start_date).days / 365., 2)
	
    def save(self, *args, **kwargs):
	"""
	Save the person model so it updates his/her number of board connections field.
	Also updates name
	"""
	
	self.name = str(self.company.name) + "   ---   " + str(self.person)
	super(Director, self).save(*args, **kwargs) # Call the "real" save() method.
	other_directors = Director.objects.filter(company=self.company)
	for director in other_directors:
	    director.person.save()
	    


class Executive(models.Model):
    """
    Represents each member of a company's executive team (i.e. management).
    """

    name = models.CharField(max_length=255, blank=True, null=True)  # This will speed up the admin
    company = models.ForeignKey(Company)
    person = models.ForeignKey(Person)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=True)
    position = models.CharField(max_length=255, blank=True)
    
    class Meta:
	verbose_name_plural = 'Executives'
	verbose_name = 'Executive'
	ordering = ['is_current', 'company', 'person', ]

    def __unicode__(self):
	return u'%s' % (unicode(self.name))

    def save(self, *args, **kwargs):
	"""
	Updates name
	"""
	
	self.name = str(self.company.name) + "   ---   " + str(self.person)
	super(Executive, self).save(*args, **kwargs) # Call the "real" save() method.
            
        


