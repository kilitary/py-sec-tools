rule _tElock_v0_98_jtushe
{
	meta:
		description = "tElock v0_98"
	strings:
		$a = {E925E4FFFF000000????????1E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
