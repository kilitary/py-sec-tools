rule _NsPack_3_4__North_Star_bqokeu
{
	meta:
		description = "NsPack 3_4 __ North Star"
	strings:
		$a = {9C60E8000000005D83ED078D85????FFFF8038010F8442020000C600018BD52B95????FFFF8995????FFFF0195????FFFF8DB5????FFFF0116606A40680010000068001000006A00FF95????FFFF85C00F846A0300}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
