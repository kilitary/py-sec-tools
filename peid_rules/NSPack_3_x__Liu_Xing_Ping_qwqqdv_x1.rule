rule _NSPack_3_x__Liu_Xing_Ping_qwqqdv
{
	meta:
		description = "NSPack 3_x __ Liu Xing Ping"
	strings:
		$a = {9C60E8000000005D83ED078D85????FFFF??38010F84??020000??0001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
