from django.db import models

class Hero(models.Model):
    """
    Data for the Home (header) section.
    """
    title = models.CharField(max_length=200, help_text="e.g. Hi, I'm XYZ.")
    subtitle = models.CharField(max_length=200, help_text="e.g. A Full-Stack Web Developer.")
    intro = models.TextField(help_text="Short intro paragraph.")
    profile_image = models.ImageField(upload_to='hero/', help_text="Hero image.")
    cv = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Downloadable CV")

    def __str__(self):
        return self.title

class AboutInfo(models.Model):
    """
    Left-column content for your About section:
    - heading: e.g. "Information About Me"
    - body: the descriptive text
    - cv: optional résumé/CV upload
    """
    heading = models.CharField(max_length=200)
    body = models.TextField()
    cv = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        help_text="Upload your résumé/CV (PDF)"
    )

    def __str__(self):
        return self.heading


class StatItem(models.Model):
    """
    The stats cards on the right of About,
    e.g. large_text="10+" small_text="Projects Completed"
    """
    large_text = models.CharField("Big Number/Text", max_length=20)
    small_text = models.CharField("Label", max_length=50)

    def __str__(self):
        return f"{self.large_text} – {self.small_text}"


class Skill(models.Model):
    """
    Your skills as level badges instead of raw percentages.
    """
    LEVEL_CHOICES = [
        ('EXP', 'Expert'),
        ('ADV', 'Advanced'),
        ('INT', 'Intermediate'),
        ('BEG', 'Beginner'),
    ]

    name = models.CharField(max_length=50)
    level = models.CharField(
        max_length=3,
        choices=LEVEL_CHOICES,
        default='IN',
        help_text="Select your proficiency level"
    )

    class Meta:
        ordering = ['-level']  # show highest levels first (EX → BE)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"


class WorkExperience(models.Model):
    """
    Timeline entries for work experience only.
    """
    start = models.CharField("From", max_length=20, help_text="e.g. 2010")
    end = models.CharField("To", max_length=20, help_text="e.g. present or 2013")
    title = models.CharField("Role", max_length=200)
    organization = models.CharField("Company", max_length=200)
    description = models.TextField()
    projects = models.TextField(
        blank=True,
        help_text="Comma-separated list of projects you worked on"
    )
    tech_stack = models.TextField(
        blank=True,
        help_text="Comma-separated list of technologies/tools used"
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order', '-start']

    def project_list(self):
        return [p.strip() for p in self.projects.split(',') if p.strip()]

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return f"{self.title} @ {self.organization}"