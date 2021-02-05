rule _NsPacK_V3_7__LiuXingPing_sazagk
{
	meta:
		description = "NsPacK V3_7 __ LiuXingPing"
	strings:
		$a = {9C60E8000000005D83ED078D??????????8039010F??????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
