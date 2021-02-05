rule _NsPack_3_1__North_Star_h__tvnhkb
{
	meta:
		description = "NsPack 3_1 __ North Star _h_"
	strings:
		$a = {9C60E8000000005D83ED078D9D????????8A033C0074108D9D????FFFF8A033C010F8442020000C603018BD52B95????FFFF8995????FFFF0195????FFFF8DB5????FFFF0116606A40680010000068001000006A00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
