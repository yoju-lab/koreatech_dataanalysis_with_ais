```
너는 훌륭한 데이터 분석가
- 현재 셀에 동작 코드 작성
- 타이타닉 생존자 데이터(titanic_df)가 있습니다. 이 데이터에서 Age 컬럼에 결측치가 다수 있습니다.  분석을 위해 Age의 NaN 값을 채우려고 합니다. 어떤 방법들이 가능할까요? 그리고 그 중 한 가지 방법(예: 중앙값으로 채우기)을 선택하여 pandas 코드로 보여주세요.

[참조]
import seaborn as sns import pandas as pd
titanic_df = sns.load_dataset('titanic') print(titanic_df.head()) print(titanic_df.shape) print(titanic_df.columns)
```

```python
titanic_df 요약 통계량 조회하는 코드 현재 셀에 작성
```

```python
age에 대한 요약 통계에 없는 대표값을 현재 셀에 코드 작성
```

```python
대상을 결측치 확인하고 머신러닝으로 채우는 코드 작성

주석 달기 [대상] titanic_df = sns.load_dataset('titanic')
```

```python