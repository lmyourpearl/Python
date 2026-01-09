import matplotlib
import matplotlib.pyplot as plt

# 한글 깨짐 방지 
plt.rc('font', family='Malgun Gothic')
matplotlib,rcParams['axes.unicode_minus']=False
cnt, PNG, UNDERBAR = 0, ' .png', '_'
CHART_NAME = 'pieChartExam'
filename = './../data/주요발생국가주간동향(4월2째주).csv'
   2:
import pandas as pd

data = pd.read_csv(filename, index_col='국가')
print(data.columns)
   3:
import pandas as pd

data = pd.read_csv(filename, index_col='국가')
print(data.columns)
   4:
import pandas as pd

data = pd.read_csv(filename, index_col='국가')
print(data.columns)
   5:
import pandas as pd

data = pd.read_csv(filename, index_col='국가')
print(data.columns)
   6:
import matplotlib
import matplotlib.pyplot as plt

# 한글 깨짐 방지 
plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False
cnt, PNG, UNDERBAR = 0, ' .png', '_'
CHART_NAME = 'pieChartExam'
filename= './../data/주요발생국가주간동향(4월2째주).csv'
   7:
import pandas as pd

data = pd.read_csv(filename, index_col='국가')
print(data.columns)
   8:
my_concern = [item for item in data,index if item in ['독일', '프랑스', '중국', '영국']]
print(my_concern)
   9:
my_concern = [item for item in data.index if item in ['독일', '프랑스', '중국', '영국']]
print(my_concern)
  10: data = data.loc[my_concern]
  11:
data = data.loc[my_concern]
chartdata = data['4월06일']
print(chartdata)
  12:
data = data.loc[my_concern]
chartdata = data['4월06일']
print(chartdata)

mylabel = chartdata.index
print(mylabel)

mycolors = ['blue', '#6AFFoo', 'yellow', '#FF003C']
  13:
plt.figure()

plt.pie(chartdata, labels = mylabel, shadow = False, explode = (0, 0.05, 0, 0),
        colors = mycolors, autopct = '%1.2f%%', startangle=90, counterclock=False)


plt.grid(True)
plt.legend(loc=4)
plt.xlabel('국가명')
#plt.xlabel('발생 건수')
plt.title('주요 국가 발생 건수')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  14:
data = data.loc[my_concern]
chartdata = data['4월06일']
print(chartdata)

mylabel = chartdata.index
print(mylabel)

mycolors = ['blue', '#6AFF00', 'yellow', '#FF003C']
  15:
plt.figure()

plt.pie(chartdata, labels = mylabel, shadow = False, explode = (0, 0.05, 0, 0),
        colors = mycolors, autopct = '%1.2f%%', startangle=90, counterclock=False)


plt.grid(True)
plt.legend(loc=4)
plt.xlabel('국가명')
#plt.xlabel('발생 건수')
plt.title('주요 국가 발생 건수')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  16:
import numpy as np
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

def getLabelFormat(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.2f}%\n({:d}명)" .format(pct, absolute)

wedges, texts, autotexts = ax.pie(chartdata, autopct=lambda pct: getLabelFormat(pct, chartdata), textprops=dict(color="w"))

ax.legend(wedges, mylabel,
          title = "국가명",
          loc = "center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("주요 국가 발생 건수")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  17:
import numpy as np

# 1. 그래프의 크기(가로 6인치, 세로 3인치)를 설정하고 
# subplot_kw=dict(aspect="equal")을 통해 파이 차트가 찌그러지지 않은 완벽한 원이 되도록 설정합니다.
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# 2. 부채꼴 안에 표시될 텍스트 형식을 지정하는 함수입니다.
# pct: 파이 차트에서 계산된 비율(%)
# allvals: 전체 데이터 리스트 (명수를 계산하기 위해 사용)
def getLabelFormat(pct, allvals):
    # 비율을 바탕으로 원래의 숫자(명수)를 역산합니다.
    absolute = int(pct/100.*np.sum(allvals))
    # '비율% (명수)' 형태로 문자열을 반환합니다. \n은 줄바꿈입니다.
    return "{:.2f}%\n({:d}명)" .format(pct, absolute)


# 3. 파이 차트를 그립니다.
# wedges: 부채꼴 조각 객체 리스트
# texts: 라벨 텍스트 객체 리스트
# autotexts: 숫자 표시(autopct) 텍스트 객체 리스트
wedges, texts, autotexts = ax.pie(chartdata, autopct=lambda pct: getLabelFormat(pct, chartdata), # 위에서 만든 함수 적용
                                  # 글자 색상을 흰색(white)으로 설정
                                  textprops=dict(color="w"))

# 4. 범례(Legend) 설정
ax.legend(wedges, mylabel,
          title = "국가명",
          loc = "center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# 5. 그래프 내부 숫자(autotexts)의 스타일을 일괄 변경합니다.
plt.setp(autotexts, size=8, weight="bold")

ax.set_title("주요 국가 발생 건수")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  18:
data = pd.read_csv(filename, index_col='국가')

fig, ax = plt.subplots(figsize(6, 3), subplot_kw=dict(aspect="equal"))

COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']

data = data.loc[COUNTRY, ['4월06일']]

print(data.values.flattern())

wedges, texts = ax.pie(data.values.flatten(), wedgeprops=dict(width=0.5), startangle=40)
  19:
data = pd.read_csv(filename, index_col='국가')

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']

data = data.loc[COUNTRY, ['4월06일']]

print(data.values.flattern())

wedges, texts = ax.pie(data.values.flatten(), wedgeprops=dict(width=0.5), startangle=40)
  20:
data = pd.read_csv(filename, index_col='국가')

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']

data = data.loc[COUNTRY, ['4월06일']]

print(data.values.flatten())

wedges, texts = ax.pie(data.values.flatten(), wedgeprops=dict(width=0.5), startangle=40)
  21:
bbox_props = dict(boxstyle="squeare, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops = dict(arrowstyle="-"),
          bbox = bbox_props, zorder = 0, va = "center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    print('ang : ', ang)
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"} [int(np.sign(x))]
    connectionstyle = "angle, angleA=0, angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle":connectionstyle})

    ax.annotate(COUNTRY[i], xy=(x,y), xytext=(1.3*np.sign(x), 1.4*y),
    horizontalignment=horizontalalignment, **kw)

ax.set_title("도우넛 그래프")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  22:
bbox_props = dict(boxstyle="squeare, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops = dict(arrowstyle="-"),
          bbox = bbox_props, zorder = 0, va = "center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    print('ang : ', ang)
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"} [int(np.sign(x))]
    connectionstyle = "angle, angleA=0, angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle":connectionstyle})

ax.annotate(COUNTRY[i], xy=(x,y), xytext=(1.3*np.sign(x), 1.4*y), horizontalignment=horizontalalignment, **kw)

ax.set_title("도우넛 그래프")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  23:
bbox_props = dict(boxstyle="squeare, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops = dict(arrowstyle="-"),
          bbox = bbox_props, zorder = 0, va = "center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    print('ang : ', ang)
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"} [int(np.sign(x))]
    connectionstyle = "angle, angleA=0, angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle":connectionstyle})

ax.set_title("도우넛 그래프")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  24:
bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops = dict(arrowstyle="-"),
          bbox = bbox_props, zorder = 0, va = "center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    print('ang : ', ang)
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"} [int(np.sign(x))]
    connectionstyle = "angle, angleA=0, angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle":connectionstyle})

    ax.annotate(COUNTRY[i], xy=(x,y), xytext=(1.3*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
    
ax.set_title("도우넛 그래프")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  25:
bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops = dict(arrowstyle="-"),
          bbox = bbox_props, zorder = 0, va = "center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    print('ang : ', ang)
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"} [int(np.sign(x))]
    connectionstyle = "angle, angleA=0, angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle":connectionstyle})

    ax.annotate(COUNTRY[i], xy=(x,y), xytext=(1.3*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
    
ax.set_title("도우넛 그래프")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')

plt.show()
  26:
data = pd.read_csv(filename, index_col='국가')

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']

data = data.loc[COUNTRY, ['4월06일']]

print(data.values.flatten())

wedges, texts = ax.pie(data.values.flatten(), wedgeprops=dict(width=0.5), startangle=40)

bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops = dict(arrowstyle="-"),
          bbox = bbox_props, zorder = 0, va = "center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    print('ang : ', ang)
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"} [int(np.sign(x))]
    connectionstyle = "angle, angleA=0, angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle":connectionstyle})

    ax.annotate(COUNTRY[i], xy=(x,y), xytext=(1.3*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
    
ax.set_title("도우넛 그래프")

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
plt.show()
  27:
fig, ax = plt.subplots()
data = pd.read_csv(filename, index_col='국가')
print(data)
  28:
fig, ax = plt.subplots()
data = pd.read_csv(filename, index_col='국가')
data
  29:
fig, ax = plt.subplots()
data = pd.read_csv(filename, index_col='국가')
data
  30:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
print(myc_concern)
  31:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
print(my_concern)
  32:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
print(my_concern)

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4워07일']]
print(filtered_data)
  33:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
print(my_concern)

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
print(filtered_data)
  34:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
my_concern

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
filtered_data

pi
  35:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
my_concern

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
filtered_data

filtered_data.index.values
  36:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
my_concern

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
filtered_data

filtered_data.index.values

totallist = []
for key in filtered_data.index.values:
    imsi = filtered_data.loc[key].values
    totallist.append([item for item in imsi])

chartdata = np.array(totallist)
print('chartdata : \n', chartdata)
  37:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
my_concern

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
filtered_data

filtered_data.index.values

totallist = []
for key in filtered_data.index.values:
    imsi = filtered_data.loc[key].values
    totallist.append([item for item in imsi])

chartdata = np.array(totallist)
print('chartdata : \n', chartdata)

color_su = len(COUNTRY)
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(color_su)*4)

inner_colors = cmap(np.arange(2*color_su))

print('inner_colors:', inner_colors)
print('outer_colors:', outer_colors)

cum_sum = chartdata.sum(axis=1)
print('cum_sum :', cum_sum)
  38:
INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_ZIE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_{CTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

as.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  39:
INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_ZIE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_PCTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

as.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  40:
INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_ZIE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_PCTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

ax.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  41:
INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_SZIE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_PCTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

ax.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  42:
INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_SIZE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_PCTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

ax.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  43:
COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
my_concern

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
filtered_data

filtered_data.index.values

totallist = []
for key in filtered_data.index.values:
    imsi = filtered_data.loc[key].values
    totallist.append([item for item in imsi])

chartdata = np.array(totallist)
print('chartdata : \n', chartdata)

color_su = len(COUNTRY)
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(color_su)*4)

inner_colors = cmap(np.arange(2*color_su))

print('inner_colors:', inner_colors)
print('outer_colors:', outer_colors)

cum_sum = chartdata.sum(axis=1)
print('cum_sum :', cum_sum)

INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_SIZE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_PCTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

ax.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  44:
fig, ax = plt.subplots()
data = pd.read_csv(filename, index_col='국가')
data

COUNTRY = ['독일', '프랑스', '중국', '영국', '이탈리아']
my_concern = [item for item in data.index if item in COUNTRY]
my_concern

data = data.loc[my_concern]
filtered_data = data[['4월06일', '4월07일']]
filtered_data

filtered_data.index.values

totallist = []
for key in filtered_data.index.values:
    imsi = filtered_data.loc[key].values
    totallist.append([item for item in imsi])

chartdata = np.array(totallist)
print('chartdata : \n', chartdata)

color_su = len(COUNTRY)
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(color_su)*4)

inner_colors = cmap(np.arange(2*color_su))

print('inner_colors:', inner_colors)
print('outer_colors:', outer_colors)

cum_sum = chartdata.sum(axis=1)
print('cum_sum :', cum_sum)

INNER_VACANT_CIRCLE_SIZE = 0.3

OUTER_PCTDISTANCE = 0.85

ax.pie(cum_sum, radius = 1, colors = outer_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_SIZE, edgecolor = 'w'),
       labels=COUNTRY, autopct='%.2f%%', pctdistance=OUTER_PCTDISTANCE)

INNER_PCTDISTANCE = 0.75

ax.pie(chartdata.flatten(), radius=1-INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       autopct = '%.2f%%', pctdistance=INNER_PCTDISTANCE)

ax.set(aspect="equal", title = '주요 국가별 중첩 파이 그래프')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')
  45:
# figure와 축(axis) 객체
fig = plt.figure(figsize = 9,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust(wspace = 0)

data = pd.read_csv(filename, index_col='국가')
data
  46:
# figure와 축(axis) 객체
fig = plt.figure(figsize=(9, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust(wspace = 0)

data = pd.read_csv(filename, index_col='국가')
data
  47:
# figure와 축(axis) 객체
fig = plt.figure(figsize=(9, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust(wspace = 0)

data = pd.read_csv(filename, index_col='국가')
  48:
# 이 코드는 주피터 노트북 '안에서' 실행하는 겁니다!
%history -g -f backup_code.py
