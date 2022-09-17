rule _tElock_v0_95_cyioyd
{
	meta:
		description = "tElock v0_95"
	strings:
		$a = {E9D5E4FFFF00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
