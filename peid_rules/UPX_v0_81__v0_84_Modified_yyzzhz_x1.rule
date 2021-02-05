rule _UPX_v0_81__v0_84_Modified_yyzzhz
{
	meta:
		description = "UPX v0_81 _ v0_84 Modified"
	strings:
		$a = {01DB??078B1E83EEFC11DB??EDB80100000001DB??078B1E83EEFC11DB11C001DB77EF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
