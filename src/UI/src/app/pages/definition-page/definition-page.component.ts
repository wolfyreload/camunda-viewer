import { Component, OnInit } from '@angular/core';
import { ITable } from 'src/modules/table-wrapper';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { TableBuilderHelper } from '../../helpers/table-builder-helper';

@Component({
  selector: 'app-definition-page',
  templateUrl: './definition-page.component.html',
  styleUrls: ['./definition-page.component.css']
})
export class DefinitionPageComponent implements OnInit {
  tableData: any;
  tableInfo: ITable | undefined;

  constructor(
    private _httpClient: HttpClient,
    private _router: Router
  ) {}

  ngOnInit(): void {
    this._httpClient.get('/api/definition').subscribe((results) => {
      this.tableInfo = TableBuilderHelper.getTableDefinitionFromResults(results);
      this.tableInfo.buttonList = ['View'];
      this.tableData = results;
    });
  }

  onRowClicked(event: any) {
    this._router.navigate(['/task', event.Key]);
  }

  onBackClick() {
    this._router.navigate(['/']);
  }
}
