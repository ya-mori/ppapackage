"""

Provide Python Aid Package

kaggleで使用するライブラリをラップしたモジュールです。
使用する際には以下のように読み込んでください。

```
import sys
sys.path.append("/${your project path }/ppappackage")
import ppapackage as ppap
```

"""
from os import path
import sys
current_dir = path.abspath(path.dirname(__file__))
sys.path.append(current_dir)

from cross_validator import CrossValidator
from cassette import ConversionCassette
from data_frame_prayer import DataFramePrayer
from ppap_exception import OverCassetteException
from ppap_exception import EmptyCassetteException
import pen

pen.read_conf()

