from django.contrib.auth.models import User
from django.db import IntegrityError, models, transaction
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from bvdata.data.managers import GastroQuerySet
from bvdata.data.utils import get_random_string_32


class BaseLocationID(models.Model):
    # id string
    id_string = models.CharField(_("unique id"), max_length=32, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        if not self.id_string:
            return self.set_string(**kwargs)

        return super(BaseLocationID, self).save(**kwargs)

    def set_string(self, **kwargs):
        self.id_string = get_random_string_32()

        try:
            with transaction.atomic():
                return self.save(**kwargs)
        except IntegrityError:
            return self.set_string(**kwargs)


class BaseLocation(models.Model):
    # create date
    created = models.DateTimeField(_("created"), auto_now_add=True)
    # update date
    updated = models.DateTimeField(_("updated"), auto_now=True)
    # name
    name = models.CharField(_("Name of location"), max_length=100)
    # street
    street = models.CharField(_("Street / No"), max_length=100)
    # cityCode
    cityCode = models.CharField(_("Postal code"), max_length=5)
    # city
    city = models.CharField(_("City"), max_length=20, default="Berlin")
    # latCoord
    latCoord = models.FloatField(_("latitude"))
    # longCoord
    longCoord = models.FloatField(_("longitude"))
    # telephone
    telephone = models.CharField(_("Telephone"), max_length=25, null=True, blank=True)
    # website
    website = models.URLField(_("Website"), null=True, blank=True)
    # email
    email = models.EmailField(_("E-mail"), null=True, blank=True)

    # otMon
    openingMon = models.TimeField(_("opening monday"), null=True, blank=True)
    closingMon = models.TimeField(_("closing monday"), null=True, blank=True)
    # otTue
    openingTue = models.TimeField(_("opening tuesday"), null=True, blank=True)
    closingTue = models.TimeField(_("closing tuesday"), null=True, blank=True)
    # otWen
    openingWed = models.TimeField(_("opening wednesday"), null=True, blank=True)
    closingWed = models.TimeField(_("closing wednesday"), null=True, blank=True)
    # otThu
    openingThu = models.TimeField(_("opening thursday"), null=True, blank=True)
    closingThu = models.TimeField(_("closing thursday"), null=True, blank=True)
    # otFri
    openingFri = models.TimeField(_("opening friday"), null=True, blank=True)
    closingFri = models.TimeField(_("closing friday"), null=True, blank=True)
    # otSat
    openingSat = models.TimeField(_("opening saturday"), null=True, blank=True)
    closingSat = models.TimeField(_("closing saturday"), null=True, blank=True)
    # otSun
    openingSun = models.TimeField(_("opening sunday"), null=True, blank=True)
    closingSun = models.TimeField(_("closing sunday"), null=True, blank=True)

    # vegan
    OMNIVORE_VEGAN = 2
    VEGETARIAN_VEGAN = 4
    VEGAN_VEGAN = 5

    VEGAN_CHOICE = (
        (OMNIVORE_VEGAN, "Ominvore (vegan labeled)"),
        (VEGETARIAN_VEGAN, "Vegetarian (vegan labeled)"),
        (VEGAN_VEGAN, "Vegan"),
    )

    vegan = models.IntegerField(_("Vegan friendly"), choices=VEGAN_CHOICE)
    # comment
    comment = models.TextField(_("Comment in German"), null=True, blank=True)
    # commentEnglish
    commentEnglish = models.TextField(_("Comment in English"), null=True, blank=True)

    # not public

    # review link
    review_link = models.URLField(
        _("review link"), max_length=255, null=True, blank=True
    )
    # if gastro is closed
    closed = models.DateField(_("closed"), null=True, default=None)
    # textfield for internal comments
    text_intern = models.TextField(_("text intern"), null=True, blank=True)

    class Meta:
        abstract = True


# districts
# we are using the old berlin districts: https://de.wikipedia.org/wiki/Berliner_Bezirke#Zeit_der_Teilung_Berlins

CHOICE_CHA = "CHARLOTTENBURG"
CHOICE_FRI = "FRIEDRICHSHAIN"
CHOICE_HEL = "HELLERSDORF"
CHOICE_HOH = "HOHENSCHÖNHAUSEN"
CHOICE_KRE = "KREUZBERG"
CHOICE_KOP = "KÖPENICK"
CHOICE_LIC = "LICHTENBERG"
CHOICE_MAR = "MARZAHN"
CHOICE_MIT = "MITTE"
CHOICE_NEU = "NEUKÖLLN"
CHOICE_PAN = "PANKOW"
CHOICE_PRE = "PRENZLAUER BERG"
CHOICE_REI = "REINICKENDORF"
CHOICE_SCH = "SCHÖNEBERG"
CHOICE_SPA = "SPANDAU"
CHOICE_STE = "STEGLITZ"
CHOICE_TEM = "TEMPELHOF"
CHOICE_TIE = "TIERGARTEN"
CHOICE_TRE = "TREPTOW"
CHOICE_WED = "WEDDING"
CHOICE_WEI = "WEISSENSEE"
CHOICE_WIL = "WILMERSDORF"
CHOICE_ZEH = "ZEHLENDORF"

DISTRICT_CHOICES = [
    (CHOICE_CHA, "Charlottenburg"),
    (CHOICE_FRI, "Friedrichshain"),
    (CHOICE_HEL, "Hellersdorf"),
    (CHOICE_HOH, "Hohenschönhausen"),
    (CHOICE_KRE, "Kreuzberg"),
    (CHOICE_KOP, "Köpenick"),
    (CHOICE_LIC, "Lichtenberg"),
    (CHOICE_MAR, "Marzahn"),
    (CHOICE_MIT, "Mitte"),
    (CHOICE_NEU, "Neukölln"),
    (CHOICE_PAN, "Pankow"),
    (CHOICE_PRE, "Prenzlauer Berg"),
    (CHOICE_REI, "Reinickendorf"),
    (CHOICE_SCH, "Schöneberg"),
    (CHOICE_SPA, "Spandau"),
    (CHOICE_STE, "Steglitz"),
    (CHOICE_TEM, "Tempelhof"),
    (CHOICE_TIE, "Tiergarten"),
    (CHOICE_TRE, "Treptow"),
    (CHOICE_WED, "Wedding"),
    (CHOICE_WEI, "Weißensee"),
    (CHOICE_WIL, "Wilmersdorf"),
    (CHOICE_ZEH, "Zehlendorf"),
]


class BaseGastro(BaseLocation):
    district = models.CharField(
        _("District"), max_length=30, null=True, choices=DISTRICT_CHOICES
    )

    # publicTransport
    publicTransport = models.CharField(
        _("Public transport"), max_length=255, null=True, blank=True
    )

    # NullBoolean Choices
    NULLBOOLEAN_NULL = None
    NULLBOOLEAN_TRUE = True
    NULLBOOLEAN_FALSE = False

    NULLBOOLEAN_CHOICE = (
        (NULLBOOLEAN_NULL, _("unknown")),
        (NULLBOOLEAN_TRUE, _("yes")),
        (NULLBOOLEAN_FALSE, _("no")),
    )

    # handicappedAccessible
    handicappedAccessible = models.NullBooleanField(
        _("Wheelchair accessible"), choices=NULLBOOLEAN_CHOICE
    )
    # handicappedAccessibleWc
    handicappedAccessibleWc = models.NullBooleanField(
        _("Wheelchair accessible toilet"), choices=NULLBOOLEAN_CHOICE
    )
    # dog
    dog = models.NullBooleanField(_("Dogs allowed"), choices=NULLBOOLEAN_CHOICE)
    # childChair
    childChair = models.NullBooleanField(_("High chair"), choices=NULLBOOLEAN_CHOICE)
    # catering
    catering = models.NullBooleanField(_("Catering"), choices=NULLBOOLEAN_CHOICE)
    # delivery
    delivery = models.NullBooleanField(
        _("Delivery service"), choices=NULLBOOLEAN_CHOICE
    )
    # organic
    organic = models.NullBooleanField(_("Organic"), choices=NULLBOOLEAN_CHOICE)
    # wlan
    wlan = models.NullBooleanField(_("Wi-Fi"), choices=NULLBOOLEAN_CHOICE)
    # glutenFree
    glutenFree = models.NullBooleanField(
        _("Gluten-free options"), choices=NULLBOOLEAN_CHOICE
    )
    # breakfast
    breakfast = models.NullBooleanField(
        _("Vegan Breakfast"), choices=NULLBOOLEAN_CHOICE
    )
    # brunch
    brunch = models.NullBooleanField(_("Brunch"), choices=NULLBOOLEAN_CHOICE)
    # seatsOutdoor
    seatsOutdoor = models.IntegerField(_("Seats outdoor"), null=True, blank=True)
    # seatsIndoor
    seatsIndoor = models.IntegerField(_("Seats indoor"), null=True, blank=True)

    # Tags

    # Restaurant
    restaurant = models.BooleanField(_("Restaurant"), default=False)
    # Imbiss
    imbiss = models.BooleanField(_("Snack bar"), default=False)
    # Eiscafe
    eiscafe = models.BooleanField(_("Ice cream parlor"), default=False)
    # Cafe
    cafe = models.BooleanField(_("Café"), default=False)
    # Bar
    bar = models.BooleanField(_("Bar"), default=False)

    # comment open
    commentOpen = models.TextField(_("Comment opening hours"), null=True, blank=True)

    submit_email = models.EmailField(_("Submitter e-mail"), null=True, blank=True)

    class Meta:
        abstract = True


class Gastro(BaseLocationID, BaseGastro):
    last_editor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("last editor"),
    )

    has_sticker = models.BooleanField(_("Sticker"), default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("data:gastro-update", args=[self.id_string])

    class Meta:
        ordering = ["name"]

    objects = GastroQuerySet.as_manager()

    # creates a dict of the model object
    def as_dict(self):
        gastro_dict = {}
        # must be in the dict and db
        gastro_dict.update(
            id=self.id_string,
            name=self.name,
            street=self.street,
            cityCode=self.cityCode,
            city=self.city,
            latCoord=self.latCoord,
            longCoord=self.longCoord,
            vegan=self.vegan,
            district=self.get_district_display(),
        )

        # opening hours
        if self.telephone is not None:
            gastro_dict.update(telephone=self.telephone)
        if self.website is not None:
            gastro_dict.update(website=self.website)
        if self.email is not None:
            gastro_dict.update(email=self.email)
        if self.openingMon is not None:
            gastro_dict.update(
                otMon=str(self.openingMon.strftime("%H:%M"))
                + " - "
                + str(self.closingMon.strftime("%H:%M"))
            )
        if self.openingTue is not None:
            gastro_dict.update(
                otTue=str(self.openingTue.strftime("%H:%M"))
                + " - "
                + str(self.closingTue.strftime("%H:%M"))
            )
        if self.openingWed is not None:
            gastro_dict.update(
                otWed=str(self.openingWed.strftime("%H:%M"))
                + " - "
                + str(self.closingWed.strftime("%H:%M"))
            )
        if self.openingThu is not None:
            gastro_dict.update(
                otThu=str(self.openingThu.strftime("%H:%M"))
                + " - "
                + str(self.closingThu.strftime("%H:%M"))
            )
        if self.openingFri is not None:
            gastro_dict.update(
                otFri=str(self.openingFri.strftime("%H:%M"))
                + " - "
                + str(self.closingFri.strftime("%H:%M"))
            )
        if self.openingSat is not None:
            gastro_dict.update(
                otSat=str(self.openingSat.strftime("%H:%M"))
                + " - "
                + str(self.closingSat.strftime("%H:%M"))
            )
        if self.openingSun is not None:
            gastro_dict.update(
                otSun=str(self.openingSun.strftime("%H:%M"))
                + " - "
                + str(self.closingSun.strftime("%H:%M"))
            )

        # gastro comments
        if self.comment is not None:
            gastro_dict.update(comment=self.comment)
        if self.commentEnglish is not None:
            gastro_dict.update(commentEnglish=self.commentEnglish)
        if self.commentOpen is not None:
            gastro_dict.update(openComment=self.commentOpen)

        # gastro public transport
        if self.publicTransport is not None:
            gastro_dict.update(publicTransport=self.publicTransport)

        # gastro description
        if self.handicappedAccessible is None:
            gastro_dict.update(handicappedAccessible=-1)
        elif self.handicappedAccessible is True:
            gastro_dict.update(handicappedAccessible=1)
        elif self.handicappedAccessible is False:
            gastro_dict.update(handicappedAccessible=0)

        if self.handicappedAccessibleWc is None:
            gastro_dict.update(handicappedAccessibleWc=-1)
        elif self.handicappedAccessibleWc is True:
            gastro_dict.update(handicappedAccessibleWc=1)
        elif self.handicappedAccessibleWc is False:
            gastro_dict.update(handicappedAccessibleWc=0)

        if self.dog is None:
            gastro_dict.update(dog=-1)
        elif self.dog is True:
            gastro_dict.update(dog=1)
        elif self.dog is False:
            gastro_dict.update(dog=0)

        if self.childChair is None:
            gastro_dict.update(childChair=-1)
        elif self.childChair is True:
            gastro_dict.update(childChair=1)
        elif self.childChair is False:
            gastro_dict.update(childChair=0)

        if self.catering is None:
            gastro_dict.update(catering=-1)
        elif self.catering is True:
            gastro_dict.update(catering=1)
        elif self.catering is False:
            gastro_dict.update(catering=0)

        if self.delivery is None:
            gastro_dict.update(delivery=-1)
        elif self.delivery is True:
            gastro_dict.update(delivery=1)
        elif self.delivery is False:
            gastro_dict.update(delivery=0)

        if self.organic is None:
            gastro_dict.update(organic=-1)
        elif self.organic is True:
            gastro_dict.update(organic=1)
        elif self.organic is False:
            gastro_dict.update(organic=0)

        if self.wlan is None:
            gastro_dict.update(wlan=-1)
        elif self.wlan is True:
            gastro_dict.update(wlan=1)
        elif self.wlan is False:
            gastro_dict.update(wlan=0)

        if self.glutenFree is None:
            gastro_dict.update(glutenFree=-1)
        elif self.glutenFree is True:
            gastro_dict.update(glutenFree=1)
        elif self.glutenFree is False:
            gastro_dict.update(glutenFree=0)

        if self.breakfast is None:
            gastro_dict.update(breakfast=-1)
        elif self.breakfast is True:
            gastro_dict.update(breakfast=1)
        elif self.breakfast is False:
            gastro_dict.update(breakfast=0)

        if self.brunch is None:
            gastro_dict.update(brunch=-1)
        elif self.brunch is True:
            gastro_dict.update(brunch=1)
        elif self.brunch is False:
            gastro_dict.update(brunch=0)

        if self.seatsOutdoor is not None:
            gastro_dict.update(seatsOutdoor=self.seatsOutdoor)
        if self.seatsIndoor is not None:
            gastro_dict.update(seatsIndoor=self.seatsIndoor)

        # tags fehlt in data import
        tags = []
        if self.restaurant is True:
            tags.append("Restaurant")
        if self.imbiss is True:
            tags.append("Imbiss")
        if self.eiscafe is True:
            tags.append("Eiscafe")
        if self.cafe is True:
            tags.append("Cafe")
        if self.bar is True:
            tags.append("Bar")
        gastro_dict.update(tags=tags)

        if self.review_link is not None:
            gastro_dict.update(reviewURL=self.review_link.split("/")[-2])

        # name
        if self.closed:
            gastro_dict.update(name=f"{self.name} - GESCHLOSSEN / CLOSED")
            gastro_dict.update(otMon="")
            gastro_dict.update(otTue="")
            gastro_dict.update(otWed="")
            gastro_dict.update(otThu="")
            gastro_dict.update(otFri="")
            gastro_dict.update(otSat="")
            gastro_dict.update(otSun="")
            gastro_dict.pop("telephone", None)

        gastro_dict.update(created=self.created.strftime("%Y-%m-%d"))

        return gastro_dict


class GastroSubmit(BaseGastro):
    gastro = models.ForeignKey(
        Gastro,
        on_delete=models.SET_NULL,
        verbose_name=_("gastro foreignkey"),
        null=True,
        blank=True,
    )

    district = models.CharField(
        _("District"), max_length=30, null=True, blank=True, choices=DISTRICT_CHOICES
    )

    def __str__(self):
        return self.name
