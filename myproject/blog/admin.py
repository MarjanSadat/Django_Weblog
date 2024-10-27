from django.contrib import admin, messages
from .models import Article, Category
from django.utils.translation import ngettext

#admin header change

admin.site.site_header = 'مدیریت وبلاگ'

# Register your models here.

# @admin.action(description='انتشار مقالات انتخاب شده')
# def make_published(modeladmin, request, queryset):
# 	queryset.update(status='p')


@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله به درستی منتشر شد.",
            "%d مقالات به درستی منتشر شد.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )



@admin.action(description='پیش نویس شدن مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
	updated = queryset.update(status="d")
	modeladmin.message_user(
		request,
		ngettext(
			"%d مقاله به درستی پیس نویس شد.",
			"%d مقالات به درستی پیس نویس شد.",
			updated,
		)
		% updated,
		messages.SUCCESS,
	)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position','title','slug','parent','status')
	list_filter = (['status'])
	search_fields = ('title','slug')
	prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','thumbnail_tag','slug','author','jpublish','is_special','status', 'category_to_str')
	list_filter = ('publish','status')
	search_fields = ('title','description')
	prepopulated_fields = {'slug' : ('title',)}
	ordering = ['status','publish'] #['-publish'] descending
	actions = [make_published, make_draft]
	
admin.site.register(Article, ArticleAdmin)
