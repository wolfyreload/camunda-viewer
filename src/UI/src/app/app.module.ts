import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { HttpInterceptorService } from '../services/http-interceptor.service';
import { DefinitionPageComponent } from './pages/definition-page/definition-page.component';
import { TableWrapperComponent } from '../modules/table-wrapper/table-wrapper.component';
import { TaskPageComponent } from './pages/task-page/task-page.component';
import { TaskHistoryPageComponent } from './pages/task-history-page/task-history-page.component';
import { EnvironmentPageComponent } from './pages/environment-page/environment-page.component';

const CUSTOM_HTTP_INTERCEPTOR = { provide: HTTP_INTERCEPTORS, useClass: HttpInterceptorService, multi: true };

@NgModule({
  declarations: [
    AppComponent,
    DefinitionPageComponent,
    TaskPageComponent,
    TaskHistoryPageComponent,
    EnvironmentPageComponent
  ],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule, TableWrapperComponent],
  providers: [CUSTOM_HTTP_INTERCEPTOR],
  bootstrap: [AppComponent]
})
export class AppModule {}
