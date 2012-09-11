DjangoAjax
==========

DjangoAjax is the example of unobtrusive ajax call in django, all you need is few additional attributes on form to make ajax enabled Django applications and almost absolutely no change in django application

##How To
List of ajax attributes: [http://codestand.feedbook.org/2012/09/django-unobtrusive-ajax.html](http://codestand.feedbook.org/2012/09/django-unobtrusive-ajax.html "Django Unobtrusive Ajax")  


##Ajax Modes
There are three modes for result set to be placed in targeted element, which must be set in data-ajax-mode attribute:

* Replace: Replace the entire content in targeted element
* Before: Insert at top in the targeted element
* After: Insert at the bottom in the targeted element

  
  
##Ajax Events
Four events are available to subscribe through attributes of Ajax call:

* data-ajax-begin: fired on the beginning of the request
* data-ajax-complete: fired on the completion of the request
* data-ajax-failure: fired on the failure of the request
* data-ajax-success: fired on the success of the request


##Loading Animation
You can set element id the data-ajax-loading="#loading" to display during Ajax call and data-ajax-loading-duration="2000" is the duration for the animation.

##Graceful Degradation
You application should be able to handle non Ajax call if javascript is not enabled, so instead of settings ajax url in form’s action, you can set it in data-ajax-url. Alternatively you can also check fr ajax call with in view method and act accordingly.

if request.is_ajax():  
return HttpResponse(str(datetime.now()))


return render_to_response('gettime.html', {'time': str(datetime.now()) })




