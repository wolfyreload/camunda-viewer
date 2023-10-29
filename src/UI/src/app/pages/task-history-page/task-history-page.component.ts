import { Component } from '@angular/core';
import { ITable } from '../../../modules/table-wrapper';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { TableBuilderHelper } from '../../helpers/table-builder-helper';

@Component({
  selector: 'app-task-history-page',
  templateUrl: './task-history-page.component.html',
  styleUrls: ['./task-history-page.component.css']
})
export class TaskHistoryPageComponent {
  variableTableData: any;
  variableTableInfo: ITable | undefined;
  tableData: any;
  tableInfo: ITable | undefined;

  private readonly definition: string | null;
  private processInstanceID: string | null;

  constructor(
    private _httpClient: HttpClient,
    private _activatedRoute: ActivatedRoute,
    private _router: Router
  ) {
    this.definition = this._activatedRoute.snapshot.paramMap.get('definition');
    this.processInstanceID = this._activatedRoute.snapshot.paramMap.get('process-instance-id');
  }

  ngOnInit(): void {
    this._httpClient.get(`/api/task-history/${this.processInstanceID}`).subscribe((results) => {
      this.tableInfo = TableBuilderHelper.getTableDefinitionFromResults(results);
      this.tableData = results;
    });
    this._httpClient.get(`/api/task-history/${this.processInstanceID}/variables`).subscribe((results) => {
      let variableTableInfo = TableBuilderHelper.getTableDefinitionFromResults(results);
      variableTableInfo.showGlobalFilter = false;
      this.variableTableInfo = variableTableInfo;
      this.variableTableData = results;
    });
  }

  onBackClick() {
    this._router.navigate(['/task', this.definition]);
  }
}
