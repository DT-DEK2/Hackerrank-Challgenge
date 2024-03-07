;With MaxSubEachDay as(
SELECT 
	[submission_date]
	,[hacker_id]
	,RANK() OVER(PARTITION BY [submission_date] order by hacker_cnt desc, hacker_id) as [Rn]
FROM (
SELECT 
	 [submission_date]
	,[hacker_id]
	,COUNT(1) as hacker_cnt
FROM submissions
GROUP BY [submission_date],[hacker_id]) hk_cnt
),
DayWiseRank as (
	Select 
		[submission_date]
		,[hacker_id]
		,DENSE_RANK() OVER (order by [submission_date]) as DayRn
	From submissions
)
,HackerCntTillDay as(
Select
	 outtr.[submission_date]
	,outtr.[hacker_id]
	,case
		when outtr.[submission_date] = '2016-03-01' then 1
		else 1 + 
		(   select count(distinct a.[submission_date]) cnt_date
			from submissions a
			where a.[hacker_id] = outtr.[hacker_id]
			and a.[submission_date] < outtr.[submission_date])
	 end as PrevCnt
	 ,[DayRn]
From DayWiseRank outtr
)
,HackerSubEachDay as(
SELECT
	 hkc.[submission_date]
	,count(distinct hkc.[hacker_id]) hacker_cnt
From HackerCntTillDay hkc
where hkc.[PrevCnt] = hkc.[DayRn]
group by hkc.[submission_date]
)
SELECT
	 hks.[submission_date]
	,hks.[hacker_cnt]
	,max_sub.[hacker_id]
	,hk.[name]
FROM HackerSubEachDay hks
JOIN MaxSubEachDay max_sub ON hks.[submission_date] = max_sub.[submission_date] AND max_sub.[Rn] = '1'
JOIN hackers hk ON max_sub.[hacker_id] = hk.[hacker_id] 