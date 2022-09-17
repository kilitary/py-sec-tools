rule _tElock_v1_00_smpxjp
{
	meta:
		description = "tElock v1_00"
	strings:
		$a = {E9E5E2FFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
