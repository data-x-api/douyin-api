# 抖音数据接口（Douyin API）：视频、评论、账号、热榜、巨量算数、星图

**抖音数据 API · 抖音评论采集 · 抖音视频播放量 · 抖音用户主页 · 抖音热搜榜 · 抖音指数（巨量算数）· 星图达人数据**

这个仓库是 [DataXAPI](https://dataxapi.com/zh/?ref=gh-douyin-api) 的抖音接口说明和能直接跑的脚本：42 个接口，一把 Key，按次付费，$0.002 起，**出错不收费**。不用登录平台账号，不用 Cookie，不开浏览器。

[免费拿 Key：试用最多 333 次，不用绑卡](https://dataxapi.com/zh/signin/?button=gh-douyin-api) · [全部接口文档](https://dataxapi.com/zh/apis/?ref=gh-douyin-api) · [接进 AI（MCP）](#接进-aimcp) · [English](#english)

最低充 $10，余额不过期；支持支付宝、微信支付和银行卡。

## 最常用的接口

DataXAPI 的客户近 30 天里调用最多的几个，从多到少：

| 接口 | 拿到什么 | 价格 |
|---|---|---|
| [抖音视频搜索](https://dataxapi.com/zh/apis/douyin/videos/search/?ref=gh-douyin-api) | 按搜索词取一页抖音视频，可按最新或最多点赞排序、按发布时间筛选：文案、作者及粉丝数、互动数。 | $0.02 一次 |
| [抖音视频评论](https://dataxapi.com/zh/apis/douyin/videos/comments/list/?ref=gh-douyin-api) | 按视频编号取一页抖音评论：正文、评论者、点赞数、回复数、发布时间。 | $0.002 一次 |
| [抖音视频播放量](https://dataxapi.com/zh/apis/douyin/videos/metrics/?ref=gh-douyin-api) | 按视频编号取一条抖音视频此刻的数字：播放数、点赞数。 | $0.002 一次 |
| [抖音视频详情](https://dataxapi.com/zh/apis/douyin/videos/get/?ref=gh-douyin-api) | 按视频编号或链接取一条抖音视频或图文：文案、作者、互动数、发布时间。 | $0.002 一次 |
| [抖音用户视频](https://dataxapi.com/zh/apis/douyin/users/videos/list/?ref=gh-douyin-api) | 按账号编号取一页这个抖音账号发布的视频，从新到旧：文案、互动数、发布时间。 | $0.002 一次 |
| [抖音用户资料](https://dataxapi.com/zh/apis/douyin/users/get/?ref=gh-douyin-api) | 按账号编号或主页链接取抖音用户资料：显示名、抖音号、简介、粉丝数、关注数、作品数、获赞总数、是否认证；完整档另有认证说明、是不是企业或店铺认证（蓝 V）、主页有没有商品橱窗、能不能直播带货、是否正在直播和直播间编号。 | $0.002 一次 |
| [抖音用户搜索](https://dataxapi.com/zh/apis/douyin/users/search/?ref=gh-douyin-api) | 按搜索词取一页抖音账号：账号编号、显示名、头像、粉丝数、作品数、获赞总数。 | $0.002 一次 |
| [抖音巨量算数关键词热度趋势](https://dataxapi.com/zh/apis/douyin/index/keywords/history/?ref=gh-douyin-api) | 按一个关键词或一次 1 到 5 个关键词，加起止日期，取每个词在抖音上逐日的搜索指数和综合指数（巨量算数，也就是抖音指数），带本期、上期和去年同期的日均值。指数是平台算出的热度分，不是搜索次数；日期是中国时间（UTC+8）的自然日。 | $0.006 一次 |

## 全部 42 个接口

### 视频、账号和评论

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [抖音视频搜索](https://dataxapi.com/zh/apis/douyin/videos/search/?ref=gh-douyin-api) | 按搜索词取一页抖音视频，可按最新或最多点赞排序、按发布时间筛选：文案、作者及粉丝数、互动数。 | $0.02 一次 | `douyin.videos.search` |
| [抖音视频评论](https://dataxapi.com/zh/apis/douyin/videos/comments/list/?ref=gh-douyin-api) | 按视频编号取一页抖音评论：正文、评论者、点赞数、回复数、发布时间。 | $0.002 一次 | `douyin.videos.comments.list` |
| [抖音视频播放量](https://dataxapi.com/zh/apis/douyin/videos/metrics/?ref=gh-douyin-api) | 按视频编号取一条抖音视频此刻的数字：播放数、点赞数。 | $0.002 一次 | `douyin.videos.metrics` |
| [抖音视频详情](https://dataxapi.com/zh/apis/douyin/videos/get/?ref=gh-douyin-api) | 按视频编号或链接取一条抖音视频或图文：文案、作者、互动数、发布时间。 | $0.002 一次 | `douyin.videos.get` |
| [抖音用户视频](https://dataxapi.com/zh/apis/douyin/users/videos/list/?ref=gh-douyin-api) | 按账号编号取一页这个抖音账号发布的视频，从新到旧：文案、互动数、发布时间。 | $0.002 一次 | `douyin.users.videos.list` |
| [抖音用户资料](https://dataxapi.com/zh/apis/douyin/users/get/?ref=gh-douyin-api) | 按账号编号或主页链接取抖音用户资料：显示名、抖音号、简介、粉丝数、关注数、作品数、获赞总数、是否认证；完整档另有认证说明、是不是企业或店铺认证（蓝 V）、主页有没有商品橱窗、能不能直播带货、是否正在直播和直播间编号。 | $0.002 一次 | `douyin.users.get` |
| [抖音用户搜索](https://dataxapi.com/zh/apis/douyin/users/search/?ref=gh-douyin-api) | 按搜索词取一页抖音账号：账号编号、显示名、头像、粉丝数、作品数、获赞总数。 | $0.002 一次 | `douyin.users.search` |
| [抖音视频榜](https://dataxapi.com/zh/apis/douyin/videos/trending/?ref=gh-douyin-api) | 取抖音最近一天的视频榜：低粉爆款、高点赞率、高完播率或高涨粉率，带播放数、点赞数、作者粉丝数。 | $0.002 一次 | `douyin.videos.trending` |
| [抖音评论回复](https://dataxapi.com/zh/apis/douyin/comments/replies/list/?ref=gh-douyin-api) | 按评论编号和它所在的视频编号取一页这条评论下的回复：正文、回复者、点赞数、发布时间。 | $0.002 一次 | `douyin.comments.replies.list` |
| [抖音话题视频](https://dataxapi.com/zh/apis/douyin/hashtags/videos/list/?ref=gh-douyin-api) | 按话题编号取一页带这个话题的抖音视频，可按综合、最多点赞或最新发布排序：文案、作者、互动数、发布时间。 | $0.002 一次 | `douyin.hashtags.videos.list` |
| [抖音达人互动与粉丝趋势](https://dataxapi.com/zh/apis/douyin/users/history/?ref=gh-douyin-api) | 按抖音账号的数字编号取最近 7 天或 30 天的变化（巨量算数）：净增粉丝、新增点赞、评论、分享和发布数，各自和上一个周期相比的变化比例，以及现在的总数；一次最多 5 个账号。给的是一个周期的合计，不是逐日序列。 | $0.002 一次 | `douyin.users.history` |
| [抖音视频转文字（文案提取、逐字稿）](https://dataxapi.com/zh/apis/douyin/videos/transcript/get/?ref=gh-douyin-api) | 给一条抖音视频的链接、分享文案或编号，返回视频里说的话：全文、每一句的起止时间和现成的 SRT 字幕，连同标题、作者和时长；可以区分说话人。每次收费，识别语音的另按视频分钟数收，没人说话不收。5 分钟以内的视频直接返回文字；超过 5 分钟、2 小时以内的先回一个凭证（job），过一会儿带着它再调这个接口取文字，按实际分钟数收，只在取到文字时收。 | $0.002 一次 | `douyin.videos.transcript.get` |
| [抖音相关视频](https://dataxapi.com/zh/apis/douyin/videos/related/?ref=gh-douyin-api) | 按视频编号取抖音在这条视频旁边推荐的一批相关视频：文案、作者、互动数。推荐结果每次可能不同。 | $0.002 一次 | `douyin.videos.related` |
| [抖音无水印视频和图片下载地址](https://dataxapi.com/zh/apis/douyin/videos/media/get/?ref=gh-douyin-api) | 给一条抖音视频或图文的编号、链接或分享口令，返回它的全部文件地址：无水印视频的各档清晰度（另给一个平台的播放跳转地址）、封面、背景音乐、图文每张图的 JPEG 和实况图视频。地址不用带请求头，签名里写了过期时间的都给出 expires_at，过期了再调一次即可。 | $0.002 一次 | `douyin.videos.media.get` |

### 热榜和搜索词

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [抖音热榜](https://dataxapi.com/zh/apis/douyin/trends/list/?ref=gh-douyin-api) | 取抖音的热点榜单：热搜榜、实时上升热点、话题热榜、热门搜索词或音乐榜，带名次和热度。 | $0.002 一次 | `douyin.trends.list` |
| [抖音搜索框联想词](https://dataxapi.com/zh/apis/douyin/keywords/related/?ref=gh-douyin-api) | 按关键词取抖音搜索框里输入这个词时给的联想词（下拉补全），按抖音列出的顺序排，一次约 10 个。只有词和名次，没有指数。 | $0.02 一次 | `douyin.keywords.related` |

### 音乐

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [抖音音乐详情（背景音乐 MP3 和使用人数）](https://dataxapi.com/zh/apis/douyin/music/get/?ref=gh-douyin-api) | 按音乐编号取一首抖音音乐：名字、作者、时长、音频文件地址（多为 MP3）、封面、抖音是否把它标为商用音乐（在抖音商用音乐库里）、是不是视频原声，以及用它发过作品的人数。音乐编号在视频的背景音乐里、音乐榜的 id 里。 | $0.002 一次 | `douyin.music.get` |

### 巨量算数（抖音指数）

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [抖音巨量算数关键词热度趋势](https://dataxapi.com/zh/apis/douyin/index/keywords/history/?ref=gh-douyin-api) | 按一个关键词或一次 1 到 5 个关键词，加起止日期，取每个词在抖音上逐日的搜索指数和综合指数（巨量算数，也就是抖音指数），带本期、上期和去年同期的日均值。指数是平台算出的热度分，不是搜索次数；日期是中国时间（UTC+8）的自然日。 | $0.006 一次 | `douyin.index.keywords.history` |
| [抖音巨量算数关键词热门视频](https://dataxapi.com/zh/apis/douyin/index/videos/search/?ref=gh-douyin-api) | 按关键词取巨量算数给出的约 20 条高指数视频：文案、链接、作者昵称、点赞数、视频指数和分类。只有一页；没有作者编号和发布时间，要这些用视频详情接口。 | $0.002 一次 | `douyin.index.videos.search` |
| [抖音巨量算数关联词](https://dataxapi.com/zh/apis/douyin/index/keywords/related/?ref=gh-douyin-api) | 按一个关键词取它在抖音上某一周的关联词（巨量算数）：搜索里一起出现的词和内容里一起出现的词，各带相关度、相关度名次、搜索指数和综合指数。指数是平台算出的热度分，不是搜索次数。 | $0.002 一次 | `douyin.index.keywords.related` |
| [抖音巨量算数实时热点](https://dataxapi.com/zh/apis/douyin/index/trends/list/?ref=gh-douyin-api) | 取巨量算数的实时热点榜或飙升热点榜，各约 30 条：名次、热点名称、热点指数、相关视频数、播放数和分类。热点指数是平台算出的热度分，不是搜索次数。 | $0.002 一次 | `douyin.index.trends.list` |
| [抖音巨量算数达人粉丝画像](https://dataxapi.com/zh/apis/douyin/index/creators/audience/get/?ref=gh-douyin-api) | 按抖音账号的数字编号取巨量算数给的粉丝画像：性别、年龄、省份、城市、城市等级、手机品牌、兴趣各段的占比。不限星图达人，只给占比，不给人数。 | $0.002 一次 | `douyin.index.creators.audience.get` |
| [抖音巨量算数品牌指数趋势](https://dataxapi.com/zh/apis/douyin/index/brands/history/?ref=gh-douyin-api) | 按品牌名和起止日期，取这个品牌在抖音上逐日的搜索指数、内容指数和传播指数（巨量算数）。指数是平台算出的分，不是次数；日期是中国时间（UTC+8）的自然日。 | $0.002 一次 | `douyin.index.brands.history` |
| [抖音巨量算数品牌指数对比](https://dataxapi.com/zh/apis/douyin/index/brands/metrics/?ref=gh-douyin-api) | 按品牌名和起止日期，取这个品牌在抖音上搜索指数、内容指数、传播指数的日均值（巨量算数），并带同行业全部品牌和前 3、5、10、15、30 名品牌的均值作参照。指数是平台算出的分，不是次数。 | $0.002 一次 | `douyin.index.brands.metrics` |
| [抖音巨量算数达人热门视频](https://dataxapi.com/zh/apis/douyin/index/creators/videos/list/?ref=gh-douyin-api) | 按抖音账号的数字编号和起止日期（最多 30 天），取巨量算数给的这个账号的热门视频，最多 20 条，按点赞数从高到低：文案、链接、发布日期、各项互动数和带来的新增粉丝数。实测平台给的都是截止日期前最后一两天发布的视频，不是整段时间里最热的；要看哪一天就把截止日期设到那一天。只有一页，没有播放数。 | $0.002 一次 | `douyin.index.creators.videos.list` |
| [抖音巨量算数达人核心指标](https://dataxapi.com/zh/apis/douyin/index/creators/metrics/?ref=gh-douyin-api) | 按抖音账号的数字编号取巨量算数给的达人核心指标：最近一周和最近一个月平均每天新增的点赞、分享、评论数和平台口径的涨粉数，以及各自和上一个周期相比的变化比例。涨粉数不是粉丝净增，比按粉丝增减算出来的大。平台没有数据的账号（各项全是 0）返回“不存在”。 | $0.002 一次 | `douyin.index.creators.metrics` |
| [抖音巨量算数关键词人群画像](https://dataxapi.com/zh/apis/douyin/index/keywords/audience/get/?ref=gh-douyin-api) | 按关键词和起止日期，取抖音上关注这个词的人群画像（巨量算数）：按年龄、性别、省份、城市、城市等级、兴趣各分一组，每组带占比和 TGI。 | $0.002 一次 | `douyin.index.keywords.audience.get` |

### 星图（达人数据和报价）

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [抖音星图达人搜索](https://dataxapi.com/zh/apis/douyin/xingtu/creators/search/?ref=gh-douyin-api) | 按昵称里的词搜索星图上的抖音达人，可按粉丝数、预期 CPM（元）、性别筛选，按预期 CPM 从低到高排：星图达人编号、昵称、所在地、内容类目、粉丝数；完整档另有植入和定制视频报价、预期 CPM（元）、预估播放数、近 30 天互动率、完播率和播放中位数、电商带货等级、性别和内容标签。其他星图接口要的达人编号从这里取。 | $0.004 一次 | `douyin.xingtu.creators.search` |
| [抖音星图达人传播数据](https://dataxapi.com/zh/apis/douyin/xingtu/creators/metrics/?ref=gh-douyin-api) | 按星图达人编号取这位抖音达人近 30 天或 90 天视频的传播数据：视频数、播放中位数、平均点赞评论分享、互动率、完播率、预期千次播放成本和单次互动成本（人民币元）。数据算的是全部视频，平台不单给商单视频的数。 | $0.004 一次 | `douyin.xingtu.creators.metrics` |
| [抖音星图达人商业报价](https://dataxapi.com/zh/apis/douyin/xingtu/creators/rates/get/?ref=gh-douyin-api) | 按星图达人编号取这位达人各种合作形式的报价和结算方式。 | $0.04 一次 | `douyin.xingtu.creators.rates.get` |
| [抖音星图达人资料](https://dataxapi.com/zh/apis/douyin/xingtu/creators/get/?ref=gh-douyin-api) | 按星图达人编号取这位抖音达人在星图上的资料：昵称、所在地、内容类目、粉丝数、性别；取一个时带抖音账号编号、抖音号、签约机构和内容标签，一次取多个（最多 50 个）时带植入和定制视频报价、预期 CPM（元）和预估播放数。 | $0.004 一次 | `douyin.xingtu.creators.get` |
| [抖音星图达人粉丝画像](https://dataxapi.com/zh/apis/douyin/xingtu/creators/audience/get/?ref=gh-douyin-api) | 按星图达人编号取这位抖音达人的粉丝画像：性别、年龄、省份、城市、城市等级、兴趣、设备、人群、消费品类和消费金额各段的粉丝数和占比。 | $0.004 一次 | `douyin.xingtu.creators.audience.get` |
| [抖音星图达人作品表现](https://dataxapi.com/zh/apis/douyin/xingtu/creators/videos/list/?ref=gh-douyin-api) | 按星图达人编号取一页这位抖音达人的视频，从新到旧，带星图给的表现数据：播放数、点赞数、完播率、互动率、时长。商单和日常视频都在里面，平台不标哪条是商单，也不能只取商单视频。 | $0.004 一次 | `douyin.xingtu.creators.videos.list` |
| [抖音星图达人内容热词](https://dataxapi.com/zh/apis/douyin/xingtu/creators/keywords/get/?ref=gh-douyin-api) | 按星图达人编号取星图从这位抖音达人少量近期视频里提出的词，约 20 个，每个带出现次数（通常只有个位数）。这些词常常只来自一两条视频，可能是一条商单：实测一个新闻媒体号返回的全是护肤品词。它不代表达人的整体内容，看内容方向请用星图内容分布接口。 | $0.002 一次 | `douyin.xingtu.creators.keywords.get` |
| [抖音星图达人星图指数](https://dataxapi.com/zh/apis/douyin/xingtu/creators/scores/get/?ref=gh-douyin-api) | 按星图达人编号取星图给这位抖音达人打的六项指数：星图指数（综合）和传播、种草、转化、合作、性价比五个分项，每项带得分、同类达人的平均分、名次和名次排在前多大比例。 | $0.008 一次 | `douyin.xingtu.creators.scores.get` |
| [抖音星图达人内容分布](https://dataxapi.com/zh/apis/douyin/xingtu/creators/content_mix/get/?ref=gh-douyin-api) | 按星图达人编号取这位抖音达人近期视频的内容分类分布：每一类的视频数和占比。用来看这位达人的内容是不是集中在某个品类。 | $0.004 一次 | `douyin.xingtu.creators.content_mix.get` |
| [抖音星图达人转化能力](https://dataxapi.com/zh/apis/douyin/xingtu/creators/conversion/get/?ref=gh-douyin-api) | 按星图达人编号取这位抖音达人带货视频的转化数据：相关视频数、播放中位数、推荐商品数，和销售额、千次播放成交额、商品价格、点击成本、组件点击次数、点击率各自所在的区间，以及带货品类。区间是平台给的文字，不是精确值；实测多数达人（包括电商等级 L4 的带货达人）各项区间都是空的（null），没有带货数据的达人返回“不存在”。 | $0.004 一次 | `douyin.xingtu.creators.conversion.get` |
| [抖音星图营销活动日历](https://dataxapi.com/zh/apis/douyin/xingtu/campaigns/list/?ref=gh-douyin-api) | 按起止时间取星图营销日历上的活动：平台大事件、电商节点、情绪节点、创意营销、行业活动，每个带名称、介绍、类型、进行到哪一步、招商期和活动期。一次给全，不翻页。 | $0.004 一次 | `douyin.xingtu.campaigns.list` |
| [抖音星图视频数据报告（播放量、完播率）](https://dataxapi.com/zh/apis/douyin/xingtu/videos/get/?ref=gh-douyin-api) | 按视频编号或链接取星图对一条抖音视频的数据报告：播放量和各项互动数，加上完播率、互动率、时长、作者粉丝数和作者的星图达人编号（可接着查这位达人的报价和传播数据）。星图收录的视频才有（多是星图达人的视频）。 | $0.004 一次 | `douyin.xingtu.videos.get` |
| [抖音星图达人粉丝画像（备用版）](https://dataxapi.com/zh/apis/douyin/xingtu/backup/creators/audience/get/?ref=gh-douyin-api) | 抖音星图达人粉丝画像的备用版，原接口取不到时改调：参数和返回相同，价格更高。 | $0.04 一次 | `douyin.xingtu.backup.creators.audience.get` |

### 备用版：原接口取不到时改调

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [抖音用户视频（备用版）](https://dataxapi.com/zh/apis/douyin/backup/users/videos/list/?ref=gh-douyin-api) | 抖音用户视频的备用版，原接口取不到时改调：参数和返回相同，价格更高。 | $0.03 一次 | `douyin.backup.users.videos.list` |
| [抖音视频搜索（备用版）](https://dataxapi.com/zh/apis/douyin/backup/videos/search/?ref=gh-douyin-api) | 抖音视频搜索的备用版，原接口取不到时改调：参数和返回相同，价格更高。 | $0.03 一次 | `douyin.backup.videos.search` |

## 真实返回长什么样

**抖音巨量算数关键词热度趋势**（`douyin.index.keywords.history`，参数 `{"since":"2026-09-01T00:00:00Z","until":"2026-09-30T00:00:00Z","keywords":["咖啡","CityWalk"]}`），录下的真实返回，个人信息换成了 …：

```json
{
  "data": {
    "items": [
      {
        "keyword": "咖啡",
        "points": [
          {
            "date": "2026-09-01T00:00:00Z",
            "search_index": 4542097,
            "composite_index": 1627826
          },
          {
            "date": "2026-09-02T00:00:00Z",
            "search_index": 4430237,
            "composite_index": 1603543
          },
          {
            "date": "2026-09-03T00:00:00Z",
            "search_index": 4439049,
            "composite_index": 1606224
          }
        ]
      }
    ]
  },
  "page": {
    "next_cursor": null,
    "cursor_expires_at": null,
    "has_more": false,
    "returned": 2
  }
}
```

**抖音视频播放量**（`douyin.videos.metrics`，参数 `{"id":"7694940173372575014"}`），录下的真实返回，个人信息换成了 …：

```json
{
  "data": {
    "item": {
      "id": "…",
      "metrics": {
        "likes": 171024,
        "views": 7234165
      }
    }
  }
}
```

每个接口都是同一种结构：列表在 `data.items`，单个在 `data.item`，下一页用 `page.next_cursor`，这次扣了多少在 `meta.billing.amount`，平台不给的字段为 `null` 并在 `meta.unavailable` 里写明。

## 快速开始

1. [拿一把 Key](https://dataxapi.com/zh/signin/?button=gh-douyin-api)（`dx_` 开头），放进环境变量：`export DATAXAPI_API_KEY=dx_...`
2. 调一次接口：

```bash
curl -G "https://api.dataxapi.com/v1/douyin/videos/search" \
  -H "Authorization: Bearer $DATAXAPI_API_KEY" \
  --data-urlencode 'query=露营'
```

3. 或者跑 `examples/` 里的脚本。只用 Python 标准库（3.9 以上）；不加 `--yes` 只报价、不调用，加了才真跑，跑完告诉你实际花了多少：

| 脚本 | 做什么 | 先看要花多少 |
|---|---|---|
| [quickstart.py](examples/quickstart.py) | 按关键词搜视频，存成 CSV（文案、作者、点赞、评论、分享、收藏） | `cd examples && python3 quickstart.py 露营装备 --pages 2` |
| [keyword_index_csv.py](examples/keyword_index_csv.py) | 1 到 5 个关键词的抖音指数（巨量算数），每天一行导出 CSV | `cd examples && python3 keyword_index_csv.py 咖啡 露营 --since 2026-10-01 --until 2026-10-31` |
| [video_metrics_csv.py](examples/video_metrics_csv.py) | 一批视频链接，导出此刻的播放数和点赞数 | `cd examples && python3 video_metrics_csv.py links.txt` |

更完整的小工具：

- [data-x-api/douyin-index-api](https://github.com/data-x-api/douyin-index-api)：抖音指数和关联词导出 CSV 的完整小工具

## 接进 AI（MCP）

Claude Code：

```bash
claude mcp add --transport http --scope user dataxapi https://api.dataxapi.com/mcp --header "Authorization: Bearer $DATAXAPI_API_KEY"
```

Cursor、Cherry Studio、WorkBuddy 等支持远程 MCP 的客户端：

```json
{
  "mcpServers": {
    "dataxapi": {
      "url": "https://api.dataxapi.com/mcp",
      "headers": {
        "Authorization": "Bearer dx_..."
      }
    }
  }
}
```

接上以后直接用中文问，比如“帮我看看这个关键词最近一个月在抖音上的热度”。AI 花钱前可以先免费查接口和价格。也可以装成技能：`npx skills add data-x-api/skills`。

## 常见问题

**要不要抖音账号、Cookie 或扫码？**

不要。只要一把 DataXAPI Key，不碰你的账号，也就不存在账号被风控的问题。

**和抖音开放平台有什么不同？**

开放平台给的是授权给你的账号自己的数据，要申请资质；这里读的是任何人都能看到的公开数据，不用申请。

**调用出错扣钱吗？**

不扣。每次返回里的 `meta.billing.amount` 写明这次扣了多少（美元）。

**抖音指数是搜索次数吗？**

不是。是平台算出的热度分，适合和自己的过去比、和另一个词比。日期是中国时间（UTC+8）的自然日，平台每天的数要晚一到两天才出。

**为什么只有一个接口有播放数？**

抖音只给作者本人看播放数，多数接口拿不到；“抖音视频播放量”这个接口专门读它。

**怎么翻页？**

列表接口一次返回一页，把返回里的 `page.next_cursor` 作为 `cursor` 传回去取下一页，每一页单独计费。

## English

Douyin API: videos, comments, accounts, hot lists, the trend index (巨量算数) and Xingtu (星图) creator data, through one key, paid per call.

No platform account, cookie or QR login. Paid per call from $0.002; errors are not charged. Free trial: up to 333 calls, no card. [Get a key](https://dataxapi.com/signin/?button=gh-douyin-api) · [All endpoints](https://dataxapi.com/apis/?ref=gh-douyin-api) · MCP: `https://api.dataxapi.com/mcp`.

## License

MIT

<sub>接口和价格取自 DataXAPI 的目录 0051cce45e9530b9、价格版本 22；以 [dataxapi.com/zh/apis](https://dataxapi.com/zh/apis/?ref=gh-douyin-api) 为准。</sub>
