rule _tElock_v0_7x__v0_84_pkaien
{
	meta:
		description = "tElock v0_7x _ v0_84"
	strings:
		$a = {60E80000C383}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
