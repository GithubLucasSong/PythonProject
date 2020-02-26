from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render
import time
class MD1(MiddlewareMixin):
    def process_request(self,request):
        max_request_per_5second = 3
        request_queue = request.session.get('request_queue',[])
        if len(request_queue) < max_request_per_5second:
            request_queue.append(time.time())
            request.session['request_queue'] = request_queue
        else:
            gap_time = time.time() - request_queue[0]
            countdown_time = 5/3 - gap_time
            if  gap_time < 5/3:
                return render(request,'time_count.html',{'time':'{:.2f}'.format(countdown_time)})
            else:
                request_queue.append(time.time())
                request.session['request_queue'] = request_queue[1:]




