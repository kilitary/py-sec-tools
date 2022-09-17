rule _Shrinker_3_3_ggxsxq
{
	meta:
		description = "Shrinker 3_3"
	strings:
		$a = {0000558BEC565775656800010000E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
