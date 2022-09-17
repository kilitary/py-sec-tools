rule _UPX_v1_03__v1_04_asidnq
{
	meta:
		description = "UPX v1_03 _ v1_04"
	strings:
		$a = {01DB??078B1E83EEFC11DB8A07??EBB80100000001DB??078B1E83EEFC11DB11C001DB73EF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
