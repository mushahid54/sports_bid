from django.contrib import admin

from miscellaneous.models import Sport, Matches, Selection, Market

class MatchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sport')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Matches, MatchesAdmin)


class SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Selection, SelectionAdmin)


class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Market, MarketAdmin)
