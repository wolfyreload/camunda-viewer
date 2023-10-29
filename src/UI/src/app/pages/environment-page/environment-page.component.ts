import { Component } from '@angular/core';
import { ITable } from '../../../modules/table-wrapper';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { TableBuilderHelper } from '../../helpers/table-builder-helper';

@Component({
  selector: 'app-environment-page',
  templateUrl: './environment-page.component.html',
  styleUrls: ['./environment-page.component.css']
})
export class EnvironmentPageComponent {
  tableData: any;
  tableInfo: ITable | undefined;

  constructor(
    private _httpClient: HttpClient,
    private _router: Router
  ) {}

  ngOnInit(): void {
    this._httpClient.get(`/api/environment`).subscribe((results) => {
      let tableInfo = TableBuilderHelper.getTableDefinitionFromResults(results);
      tableInfo.buttonList = ['View'];
      this.tableInfo = tableInfo;
      this.tableData = results;
    });
  }

  onRowClicked(event: any) {
    this._httpClient.post(`/api/environment/${event.EnvironmentName}`, null).subscribe(() => {
      this._router.navigate(['/definition']);
    });
  }
}
