import { Component, EventEmitter, Input, Output, ViewChild } from '@angular/core';
import { ITable } from './interfaces/ITable';
import { Table, TableModule } from 'primeng/table';
import { NgForOf, NgIf } from '@angular/common';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-table-wrapper',
  templateUrl: './table-wrapper.component.html',
  styleUrls: ['./table-wrapper.component.css'],
  imports: [TableModule, NgIf, NgForOf, ButtonModule],
  standalone: true
})
export class TableWrapperComponent {
  @Input() tableInfo: ITable | undefined;
  @Input() tableData!: object[];
  @Output() rowClicked = new EventEmitter<any>();

  @ViewChild('table') table!: Table;

  onRowClick(rowData: any) {
    this.rowClicked.emit(rowData);
  }

  // Custom filter function for global search
  globalFilter(table: Table, event: Event) {
    if (!table) {
      return;
    }

    const value = (event.target as HTMLInputElement).value;
    table.filterGlobal(value, 'contains');
  }
}
