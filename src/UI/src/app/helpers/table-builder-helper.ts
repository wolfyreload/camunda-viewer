import { ITable } from '../../modules/table-wrapper';

export class TableBuilderHelper {
  static getTableDefinitionFromResults(results: any) {
    let resultList = results as any[];
    let keys = Object.keys(resultList[0]);

    let tableInfo: ITable = {
      columnList: keys,
      showGlobalFilter: true
    };
    return tableInfo;
  }
}
