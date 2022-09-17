rule _tElock_v0_71_inxdfp
{
	meta:
		description = "tElock v0_71"
	strings:
		$a = {60E8ED100000C383}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
