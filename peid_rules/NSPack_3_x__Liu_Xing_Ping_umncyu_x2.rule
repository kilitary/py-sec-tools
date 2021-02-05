rule _NSPack_3_x__Liu_Xing_Ping_umncyu
{
	meta:
		description = "NSPack 3_x __ Liu Xing Ping"
	strings:
		$a = {9C60E8000000005D83ED078D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
