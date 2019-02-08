from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import todoItem



def todoAppView(request):
	allTodoItem=todoItem.objects.all()
	return render(request, 'todo.html',
		{'all_item':allTodoItem})

def addTodo(request):
	#ccreate todo object
	#save
	#redirect the browser to /todo/
	c=request.POST['content']
	newItem=todoItem(content=c)
	newItem.save()
	return HttpResponseRedirect('/todo/')

def delTodo(request, todo_id):
	itemToDel = todoItem.objects.get(id=todo_id)
	itemToDel.delete()
	return HttpResponseRedirect('/todo/')



