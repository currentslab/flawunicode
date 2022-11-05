# flawunicode

Detect unreadable unicode text

Ever encounter any text when crawl text from the internet or inside your raw corpus?

```
srtytyrtyrty
Á¶ÀÌ½ÃÆ¼, ¡®3on3 ÇÁ¸®½ºÅ¸ÀÏ¡¯ 2Á¾ÀÇ ¿¡µð¼Ç ¹øµé Ãâ½Ã
��>+ٽT}$@�������Э����ٗ_���=���e��
```

This is what flawunicode aims to pick these out for you. flawunicode ranks each unicode text and output a score of -1 to 1 which indicates the "completeness" of the unicode text. If the text has a score of lower than 0.4, it is likely this text is not readable by human.

## Usage

```python
import flawunicode
text = "fdsfdxvdhjkf"
flawunicode.detect(text)
>> 0.2727272727272727
flawunicode.detect("Hello World!")
>> 0.6439393939393939
```


## Note

The underlying statistic came from news corpus in [currents api](https://currentsapi.services/en) database. So social network style text maybe rank with low score. You just need to calculate your own frequently used bi-gram characters and it should be fine.



