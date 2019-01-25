from django.contrib import admin

from hearts_core.models import Document, Content, Vote


class ContentInLine(admin.TabularInline):
    model = Content
    extra = 0


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'owner', 'was_created_recently')
    search_fields = ['title', 'owner']
    list_filter = ['created_on']
    inlines = [ContentInLine]


class ContentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'document', 'created_on')
    list_filter = ['created_on', 'document']
    search_fields = ['text', 'document']


class VoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_on')
    list_filter = ['created_on', 'content']
    search_fields = ['content']


admin.site.register(Document, DocumentAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Vote, VoteAdmin)
