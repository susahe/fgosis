from django.contrib import admin
from course.models import Course , Topic,Lesson,Activity,CourseModule,Teachers_Diary,CourseGroup,Theory_Lesson_Schedule ,Practical_Lesson_Schedule


# Add in this class to customized the Admin Interface
class CourseAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', 'code','created_at',)
	
class CourseModuleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', )
	
class TopicAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
class Teachers_DiaryAdmin(admin.ModelAdmin):
	list_display = ("activity",)
	
class LessonAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('name', )

class CourseGroupAdmin(admin.ModelAdmin):
	list_display = ('name', )


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule, CourseModuleAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Teachers_Diary,Teachers_DiaryAdmin)
admin.site.register(CourseGroup,CourseGroupAdmin)
admin.site.register(Theory_Lesson_Schedule)
admin.site.register(Practical_Lesson_Schedule)
