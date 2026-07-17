# Transportation 页面维护手册（航线信息源与验证方法）

> 本文件不会被发布到网站（`_notes/` 下划线目录 Jekyll 不处理），仅供维护者使用。
> 对应页面：`_pages/transportation.md`（https://cyber-science.org/2026/transportation/）
> 上次全面验证：**2026-07-17**。建议在会前（2026 年 9 月底–10 月）复查一次。

## 1. 复查时要做什么

1. 逐条核对"直飞航线表"中的航线是否仍在运营（重点：季节性/低频航线，见 §4 风险清单）；
2. 核对 SkyBus 票价（页面写的是单程 A$24.60 / 往返 A$43.40）；
3. 把 §5 中"会期前将开航"的新航线加进表格（若已确认开航）；
4. 更新页面表格下方的"信息核实日期"（现为 July 2026）。

复查最快的方式：让 Claude 读本文件后按 §3 的方法并行验证，无需从头调研。

## 2. 基线信息源

| 用途 | 来源 | 说明 |
|---|---|---|
| 航线总表基线 | https://en.wikipedia.org/wiki/Melbourne_Airport 的 "Airlines and destinations" | 社区维护、更新快，但有个别错漏（本次漏了厦航，多列了经停航班），**必须逐条核验** |
| 航线变动新闻 | https://www.aeroroutes.com/ | 航班时刻变动的权威行业源，可搜 "aeroroutes melbourne <airline>" |
| 机场官方新闻稿 | https://www.melbourneairport.com.au/corporate/ | 新开航线均有 press release；另有航司名录 https://www.melbourneairport.com.au/airline/ |
| 实时执飞记录 | trip.com 航班状态页（如 https://us.trip.com/flights/status-mu737/ ）| 验证"最近是否真的在飞"最可靠的可抓取来源 |
| SkyBus 票价 | https://www.skybus.com.au/fares/ | 官方票价页 |

**抓取注意（2026-07 实测）**：`visitmelbourne.com`、`flightsfrom.com`、`airportia.com`、`directflights.com`、`flightera.net` 拒绝程序抓取（403），只能用搜索摘要；`visitvictoria.com`、Wikipedia、aeroroutes、trip.com 状态页、多数航司官网可直接抓取。

## 3. 验证方法（本次流程，可复用）

1. 以 Wikipedia 表格为基线列出"航司 × 航线"清单；
2. 按地区分 4 组并行验证（中国 A / 中国 B / 港台日韩 / 东南亚），每组一个检索代理；
3. 每条航线的证据优先级：**航司官网（开航页/目的地页/时刻表）> 机场官方新闻稿 > 行业媒体（AeroRoutes、Executive Traveller、CAPA）> 航班追踪站近期执飞记录**；
4. 每条给出结论：CONFIRMED / SEASONAL（注明季节窗口）/ SUSPENDED / NOT CONFIRMED；
5. 特别注意：季节窗口是否覆盖**会期 2026-11-09 ~ 11-13**；"直飞"是否实为经停（本次 Batik Air 吉隆坡线即经停巴厘岛）。

## 4. 当前表格状态与复查风险清单（截至 2026-07-17）

### 中国大陆（10 城，全部已验证）

| 城市 | 航司 | 班次（07/2026） | 主要依据 | 复查风险 |
|---|---|---|---|---|
| 北京(首都T3) | 国航 CA165/166 | 3–5班/周 | trip.com 执飞记录；airchina.com.au | 低 |
| 上海浦东 | 东航 MU737/738 | 每天 | trip.com 执飞记录 | 低 |
| 上海浦东 | 吉祥 HO1655/1656 | 3–4班/周 | global.juneyaoair.com；机场新闻稿 | 低 |
| 广州 | 南航 CZ321/322+343/344 | **每天2班** | csair.com 澳洲专页 | 低 |
| 深圳 | 深航 ZH811/812 | 3班/周 | 深航官方开航页（2025-12开航） | 中（新航线） |
| 成都天府 | 川航 3U3885/3886 | 2班/周 | AeroRoutes | 中 |
| 厦门 | 厦航 MF803/804 | 每天 | xiamenair.com/en-au；机场航司名录 | 低 |
| 杭州 | 首都航空 JD385/386 | ≤3班/周 | 2026夏秋航季信息 | **高（班次波动）** |
| 青岛 | 首都航空 JD461/462 | 1–2班/周 | AeroRoutes（2026-01复航） | **高（有停飞史，务必复查）** |
| 海口 | 海航 HU483/484 | 2–3班/周 | 机场新闻稿 | 中 |

### 港台日韩

| 航线 | 状态 | 备注 |
|---|---|---|
| 国泰 香港 | ✅ 每天多班（CX105等） | 低风险 |
| 澳航 香港 QF29/30 | ✅ 每天 | 低风险 |
| **香港航空 HX13/14** | ❌ 季节性（12月–3月），**不覆盖会期，已从表格移除** | 复查时确认冬季班期是否提前到11月，若提前可加回 |
| 华航 台北 CI57/58 | ✅ 4班/周 | china-airlines.com 官网已验证 |
| JAL 东京成田 JL773/774 | ✅ 夏季3班/周，冬季（≥10月底）加密至每天 | 低风险 |
| 澳航 东京成田 QF79/80 | ✅ 每天（12–3月11班/周）；**是成田不是羽田**（澳航已放弃羽田时刻） | 低风险 |
| **韩亚 首尔仁川** | ⚠️ 季节性（约10月底–3月底），**覆盖会期，已以 seasonal 标注加入表格** | **复查时确认 2026/27 冬季班期已开卖**（依据：flyasiana.com 公告 + AeroRoutes "OZ NW26"） |

### 东南亚（已验证）

新加坡（SQ 每天~5班含A380 / 酷航 / 捷星 / 澳航QF37-38）、吉隆坡（马航~2班/天、亚航X 每天；**Batik Air 为经停巴厘岛，勿列为吉隆坡直飞**）、曼谷（泰航TG465/466每天、捷星~5班/周）、胡志明（越航每天、越捷、捷星）、河内（越航2–3班/周）、雅加达（嘉鲁达4班/周）、巴厘岛（捷星/澳航/维珍/嘉鲁达/Batik）、马尼拉（菲航每天、宿务~5班/周）、文莱（皇家文莱~5班/周）。

### 其他地区（未做官网级验证，来自 Wikipedia 2026-07 版本）

中东（卡塔尔多哈、阿联酋迪拜、阿提哈德阿布扎比）、美国（洛杉矶QF/UA/DL、旧金山UA、达拉斯QF）、新西兰四城、南美圣地亚哥（LATAM）、德里（印航；澳航季节性）、科伦坡（斯里兰卡航空）。复查时如有余力可补验。

## 5. 会期前预计开航的新航线（复查时确认后可加入表格）

| 航线 | 预告开航日期 | 来源（2026-07） |
|---|---|---|
| 捷星 墨尔本—科伦坡 | 2026-08-25 | Wikipedia 航线表 |
| 澳航 墨尔本—伦敦希思罗（复航） | 2026-10-25 | 已写入页面（"from late October 2026"） |
| 芬兰航空 墨尔本—曼谷（—赫尔辛基） | 2026-10-26 | Wikipedia 航线表 |

## 6. 机场交通信息源（页面第二节）

- SkyBus 票价/班次：https://www.skybus.com.au/fares/ 、https://www.skybus.com.au/melbourne-city-express/ （现为 A$24.60 单程 / A$43.40 往返，24小时运营，高峰约10分钟一班）；
- 会场地址：RMIT City campus, 124 La Trobe Street, Melbourne VIC 3000（紧邻 Melbourne Central 站）；
- Free Tram Zone：https://www.ptv.vic.gov.au/more/travelling-on-the-network/free-tram-zone/ ；
- 出租车估价 A$55–75 为通行估计值，复查时可再校对。
