rule _tElock_v0_92a_kimygs
{
	meta:
		description = "tElock v0_92a"
	strings:
		$a = {E97EE9FFFF00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
