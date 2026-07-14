# %%

import pandas as pd

df = pd.read_excel('titanic.xls')
df.head(3)
# %%
df['sex'].head()
# %%
df['survived'].head()
# %%
df['sex'].value_counts()
# %%
df['survived'].value_counts()
# %%
df.groupby('sex')['survived'].mean()
# %%
import matplotlib.pyplot as plt
import seaborn as sns

pclass_survival = df.groupby('pclass')['survived'].mean()
pclass_survival
# %%
plt.bar(pclass_survival.index, pclass_survival.values)
# %%
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.xticks([1, 2, 3])
plt.title('Survival Rate by Pclass')
plt.bar(pclass_survival.index, pclass_survival.values)
# %%
cross_tab = pd.crosstab(index=df['pclass'], columns=df['sex'], values=df['survived'], aggfunc='mean')
print(cross_tab)
# %%
sns.heatmap(cross_tab, annot=True, cmap='coolwarm')
# %%
# %% [3] 등급별 성별 생존율 교차 분석
import pandas as pd

# pd.crosstab을 사용해 pclass와 sex를 교차시키고 survived의 평균을 구합니다.
survival_table = pd.crosstab(
    index=df['pclass'],       # 행(세로축)에는 객실 등급을 둔다
    columns=df['sex'],        # 열(가로축)에는 성별을 둔다
    values=df['survived'],    # 칸에 채워질 데이터는 생존 여부로 한다
    aggfunc='mean'            # 그 데이터들을 묶어서 '평균(생존율)'을 낸다
)

print(survival_table)
# %%
# %% [4] 등급별 성별 생존율 시각화 (막대그래프)
import matplotlib.pyplot as plt

# 판다스 데이터프레임 자체에 내장된 plot 기능을 쓰면 matplotlib으로 자동 연동됩니다.
# kind='bar'는 막대그래프, rot=0은 x축 글씨(pclass)를 회전하지 않고 똑바로 세우는 옵션입니다.
survival_table.plot(kind='bar', rot=0, figsize=(8, 5))

# 차트 디테일 설정 (질문자님이 아까 쓰신 문법 활용!)
plt.title('Survival Rate by Pclass and Sex')
plt.xlabel('Pclass (Passenger Class)')
plt.ylabel('Survival Rate')
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 가로 눈금선 추가로 가독성 높이기

plt.show()
# %%
# %% [5] 등급별 성별 생존율 시각화 (히트맵)
import matplotlib.pyplot as plt

# matshow를 쓰면 표 형태의 데이터를 색상으로 표현해 줍니다.
plt.figure(figsize=(6, 5))
plt.matshow(survival_table, cmap='Blues', fignum=1)  # 파란색 농도로 표현
plt.colorbar(label='Survival Rate')                  # 우측에 색상 기준바 표시

# 축 레이블 매칭하기
plt.xticks([0, 1], labels=['Female', 'Male'])
plt.yticks([0, 1, 2], labels=['1st', '2nd', '3rd'])
plt.title('Survival Rate Heatmap', pad=20)

# 칸 마다 실제 숫자 적어주기 (디테일)
for i in range(len(survival_table.index)):
    for j in range(len(survival_table.columns)):
        val = survival_table.iloc[i, j]
        plt.text(j, i, f'{val:.2f}', ha='center', va='center', 
                 color='white' if val > 0.5 else 'black')

plt.show()
# %%
# %% [5] seaborn으로 히트맵 깔끔하게 그리기
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 5))

# annot=True: 칸 안에 숫자 적기
# fmt='.2f': 소수점 둘째 자리까지 표시
# cmap='Blues': 파란색 테마 적용
sns.heatmap(survival_table, annot=True, fmt='.2f', cmap='Blues')

plt.title('Survival Rate Heatmap by Pclass and Sex')
plt.show()
# %%
# %% [1] 성별 생존율 기본 그래프
import seaborn as sns
import matplotlib.pyplot as plt

# data에 데이터프레임을 넣고, x축과 y축에 컬럼 이름만 문자열로 쏙 넣어주면 끝!
sns.barplot(data=df, x='sex', y='survived')
plt.show()
# %%
sns.countplot(data=df, x='sex')
# %%
sns.histplot(data=df, x='age', kde = True)
# %%
sns.scatterplot(data = df, x = 'age', y = 'fare')
# %%
plt.figure(figsize = (8,5))

sns.barplot(data = df, x = 'pclass', y = 'survived', hue = 'sex')
plt.title('Survival Rate by Pclass and Sex (Seaborn)')
plt.show()
# %%
sns.set_theme(style="whitegrid")

sns.barplot(data = df, x = 'pclass', y = 'survived', hue = 'sex')
plt.title('Survival Rate by Pclass and Sex (Seaborn)')
plt.show()
# %%
