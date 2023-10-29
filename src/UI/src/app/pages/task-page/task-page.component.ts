import { Component, OnInit } from '@angular/core';
import { ITable } from '../../../modules/table-wrapper';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { TableBuilderHelper } from '../../helpers/table-builder-helper';

@Component({
  selector: 'app-task-page',
  templateUrl: './task-page.component.html',
  styleUrls: ['./task-page.component.css']
})
export class TaskPageComponent implements OnInit {
  tableData: any;
  tableInfo: ITable | undefined;
  private definition: string | null;

  constructor(
    private _httpClient: HttpClient,
    private _activatedRoute: ActivatedRoute,
    private _router: Router
  ) {
    this.definition = this._activatedRoute.snapshot.paramMap.get('definition');
  }

  ngOnInit(): void {
    this._httpClient.get(`/api/task/${this.definition}`).subscribe((results) => {
      let tableInfo = TableBuilderHelper.getTableDefinitionFromResults(results);
      tableInfo.buttonList = ['View'];
      this.tableInfo = tableInfo;
      this.tableData = results;
    });
  }

  onRowClicked(event: any) {
    let processInstanceID = event.ProcessInstanceID;
    this._router.navigate(['/task', this.definition, processInstanceID]);
  }

  onBackClick() {
    this._router.navigate(['/definition']);
  }
}
