# ETL Character Database

This project relies on the dataset provided by **etlcdb**.

## To do

1. <span style="color: #ff0000">To retrieve the data needed for this project, you therefore have to request the access to those on their website: http://etlcdb.db.aist.go.jp/download-request</span>

2. Once all the ZIP files downloaded, you will have to put the extracted folders in this directory.

As a result, you should have the following structure:

```
etl_data/ETL1
etl_data/ETL2
...
etl_data/ETL9G
```

3. Launch the extractor by running `python etl_extractor.py` from the root directory

Once you have run the extractor, you will have a new **images** directory.
Each sub-directory will correspond to one of the previous directory (ETL1, ETL2, ...), each containing multiples sub-directories as well.

These directories are in fact each characters organised in a folder named after their hexadecimal unicode value.

Example:

`images/ETL1/0x00a5` => "0x00a5" corresponds to "¥" coming from the ETL1 folder.

4. You have all the assets you need! However, you will just have to reorganize your folders so as to match with this project's structure. Please follow the remaining steps in the main README
