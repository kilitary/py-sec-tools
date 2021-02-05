rule _NsPacK_V3_1__LiuXingPing_ibmxhm
{
	meta:
		description = "NsPacK V3_1 __ LiuXingPing"
	strings:
		$a = {9C60E8000000005D83ED078D9D????????8A033C0074}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
