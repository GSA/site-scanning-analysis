import { DataFrame } from 'dataframe-js';

export class SnapshotLoader {
  private snapshotUrl: string;
  private dataFrame?: DataFrame;

  constructor(snapshotUrl: string) {
    this.snapshotUrl = snapshotUrl;
  }

  async load(): Promise<DataFrame> {
    this.dataFrame = await DataFrame.fromCSV(this.snapshotUrl);
    return this.dataFrame;
  }

}