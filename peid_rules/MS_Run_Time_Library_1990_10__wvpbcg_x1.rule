rule _MS_Run_Time_Library_1990_10__wvpbcg
{
	meta:
		description = "MS Run_Time Library 1990 _10_"
	strings:
		$a = {E8????2EFF2E????BB????E8????CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
