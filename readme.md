1. one off generate schema use json schema generator
2. upload schema to s3 - `s3://data-platform-schema/`.

3. unit test/CI: download production schema
4. compare local schema with production schema
5. (optionally) handle datatime check