import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DefinitionPageComponent } from './pages/definition-page/definition-page.component';
import { TableWrapperComponent } from '../modules/table-wrapper/table-wrapper.component';
import { TaskPageComponent } from './pages/task-page/task-page.component';
import { TaskHistoryPageComponent } from './pages/task-history-page/task-history-page.component';
import { EnvironmentPageComponent } from './pages/environment-page/environment-page.component';

const routes: Routes = [
  { path: '', component: EnvironmentPageComponent },
  { path: 'definition', component: DefinitionPageComponent },
  { path: 'task/:definition', component: TaskPageComponent },
  { path: 'task/:definition/:process-instance-id', component: TaskHistoryPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes), TableWrapperComponent],
  exports: [RouterModule]
})
export class AppRoutingModule {}
