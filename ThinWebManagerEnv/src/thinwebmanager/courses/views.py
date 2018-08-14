from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Course
from .forms import CourseForm


class CourseObjectMixin(object):
    model = Course

    def get_object(self):
        course_id = self.kwargs.get("course_id")
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=course_id)
        return obj


class CourseCreateView(View):
    template_name = "courses/course_create.html"

    def get(self, request, *args, **kwargs):
        form = CourseForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class CoursesListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_query_set(self):
        return Course.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"courses": self.get_query_set()})


class CourseDetailView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"

    def get(self, request, course_id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseForm(instance=obj)
            context["form"] = form
            context["obj"] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()

        if obj is not None:
            form = CourseForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context["form"] = form
            context["obj"] = obj
        return render(request, self.template_name, context)


class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context["obj"] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["obj"] = None
            return redirect("/courses/")
        return render(request, self.template_name, context)
