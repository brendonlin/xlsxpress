# XlsxPress

XlsxPress 是一个提供 Excel 文件和关系型数据库之间快速传输的工具。

XlsxPress 不需要用户指定 Schema 和大量的配置，鼓励**先传输-再转换**的思想。尽可能帮助用户自动解析数据的结构和所需配置。

参考命令

```python
python .\upload.py -p .\tests\data\category_label.xlsx -c local_mysql
```
