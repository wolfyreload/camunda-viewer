import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable()
export class HttpInterceptorService implements HttpInterceptor {
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // You can modify the request here before it is sent to the server
    // For example, you can add headers or authentication tokens to the request

    // Add api url for all requests
    const modifiedRequest = request.clone({
      url: environment.apiUrl + request.url
    });

    // Continue with the modified request
    return next.handle(modifiedRequest);
  }
}
