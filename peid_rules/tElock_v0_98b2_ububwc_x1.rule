rule _tElock_v0_98b2_ububwc
{
	meta:
		description = "tElock v0_98b2"
	strings:
		$a = {E91BE4FFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
