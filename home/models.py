from django.db import models


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class PortfolioProfile(models.Model):
    name = models.CharField(max_length=120, default="Sathwik Chinthakindhi")
    headline = models.CharField(
        max_length=200,
        default="Python Developer | Software Engineer | Full Stack Developer | Data Analytics",
    )
    short_intro = models.TextField(blank=True)
    about = models.TextField(blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        help_text="Upload your current PDF resume.",
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio profile"
        verbose_name_plural = "Portfolio profile"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    technologies = models.CharField(
        max_length=400,
        help_text="Separate technologies with commas, e.g. Python, Django, YOLOv8",
    )

    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    thumbnail = models.ImageField(
        upload_to="projects/",
        blank=True,
    )

    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=180)
    issuer = models.CharField(max_length=180)
    issue_date = models.DateField(blank=True, null=True)

    credential_id = models.CharField(max_length=180, blank=True)
    credential_url = models.URLField(blank=True)
    certificate_file = models.FileField(
        upload_to="certificates/",
        blank=True,
        help_text="Upload a certificate image or PDF.",
    )

    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-issue_date", "-created_at"]

    def __str__(self):
        return f"{self.title} — {self.issuer}"


class Experience(models.Model):
    organisation = models.CharField(max_length=180)
    role = models.CharField(max_length=180)
    employment_type = models.CharField(
        max_length=80,
        blank=True,
        help_text="e.g. Internship, Training, Full-time",
    )

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)

    description = models.TextField()
    technologies = models.CharField(max_length=400, blank=True)
    organisation_url = models.URLField(blank=True)

    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-start_date", "-id"]
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.role} — {self.organisation}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Programming Languages"),
        ("web", "Web Development"),
        ("frameworks", "Frameworks and Libraries"),
        ("database", "Databases"),
        ("ai_ml", "AI and Machine Learning"),
        ("tools", "Tools and Platforms"),
        ("concepts", "Core Concepts"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="concepts",
    )
    proficiency = models.PositiveSmallIntegerField(
        default=70,
        help_text="Optional percentage from 0 to 100.",
    )

    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"],
                name="unique_skill_name_category",
            ),
            models.CheckConstraint(
                check=models.Q(proficiency__gte=0, proficiency__lte=100),
                name="skill_proficiency_0_to_100",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"    