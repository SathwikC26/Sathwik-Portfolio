from django.contrib import admin
from .models import (
    PortfolioProfile,
    Project,
    Certificate,
    Experience,
    Skill,
    ContactMessage,
)

@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "updated_at")

    def has_add_permission(self, request):
        # Keep one editable profile record.
        if PortfolioProfile.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "featured",
        "is_published",
        "display_order",
        "updated_at",
    )
    list_filter = ("featured", "is_published")
    search_fields = ("title", "description", "technologies")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("featured", "is_published", "display_order")
    ordering = ("display_order", "-created_at")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "issuer",
        "issue_date",
        "is_published",
        "display_order",
    )
    list_filter = ("issuer", "is_published")
    search_fields = ("title", "issuer", "credential_id")
    list_editable = ("is_published", "display_order")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "role",
        "organisation",
        "start_date",
        "end_date",
        "is_current",
        "is_published",
        "display_order",
    )
    list_filter = ("is_current", "is_published", "employment_type")
    search_fields = ("role", "organisation", "description")
    list_editable = ("is_current", "is_published", "display_order")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "is_published", "display_order")
    list_filter = ("category", "is_published")
    search_fields = ("name",)
    list_editable = ("proficiency", "is_published", "display_order")
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = (
        "-created_at",
    )