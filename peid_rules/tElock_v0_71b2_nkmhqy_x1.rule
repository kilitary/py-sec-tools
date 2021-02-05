rule _tElock_v0_71b2_nkmhqy
{
	meta:
		description = "tElock v0_71b2"
	strings:
		$a = {60E844110000C383}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
