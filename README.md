# BiliBili-Video-Recommendation

## B站API示例：
"https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=76&page=1&pagesize=100&jsonp=jsonp&time_from=20220123&time_to=20220130"

## 筛选规则如下：
1、七天的时间范围

2、推荐的视频不会重复

3、按照播放数与时长的比例--（综合分数）进行排序

4、每个分区预先获取100+个视频，通过数据分析后按比例选出头部视频

5、将每个分区的头部视频合到一起形成100个视频，再根据视频的综合分数进行从高到底的排序，每次得到100个视频

6、推荐的视频将按照图片-链接-介绍的形式存在文件中

## 分区及其编号代码以及各分区占比如下：
	76：美食区（20%）
	17：单机联机游戏（15%）
	95：数码（15%）
	75：动物区（12%）
	124：趣味科普人文（7%）
	85：短片（5%）
	86：特摄（5%）
	182：影视杂谈（5%）
	21：日常（2%）
	71：综艺（2%）
	122：野生技术协会（2%）
	138：搞笑（2%）
	161：手工（2%）
	172：手机游戏（2%）
	183：影视剪辑（2%）
	184：预告（2%）
	
## 构建好的exe文件见Release

## About Using
请勿用于商业用途 ！

PLEASE DO NOT USE IT FOT BUSINESS !
