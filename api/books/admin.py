from django.contrib import admin
from django.utils import timezone

from books.models import Author, Book, BookSold, Publisher, Tag, Sale


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('artistic_name',)
        }),
        ('User information', {
            'classes': ('collapse',),
            'fields': ('user',),
        }),
    )


class AuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'publisher', 'is_new', 'created_at', 'updated_at')
    list_display_links = ('title',)
    # list_select_related = ('publisher',)

    # filter_horizontal = ['tags']
    # filter_vertical = ['tags']
    # raw_id_fields = ['tags']

    search_fields = ['title']

    empty_value_display = '-empty-'

    inlines = [
        AuthorInline,
    ]
    exclude = ('authors',)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    actions_on_top = True
    actions_on_bottom = False
    actions = ['make_republished']

    def make_republished(self, request, queryset):
        rows_updated = queryset.update(publication_date=timezone.now().date())
        if rows_updated == 1:
            message_bit = "1 book was"
        else:
            message_bit = "%s books were" % rows_updated
        self.message_user(request, "%s successfully marked as republished." % message_bit)
    make_republished.short_description = "Mark selected stories as republished"


@admin.register(BookSold)
class BookSoldAdmin(admin.ModelAdmin):
    actions = None


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
