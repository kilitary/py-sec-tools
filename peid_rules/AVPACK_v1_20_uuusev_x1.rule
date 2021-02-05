rule _AVPACK_v1_20_uuusev
{
	meta:
		description = "AVPACK v1_20"
	strings:
		$a = {501E0E1F160733F68BFEB9????FCF3A506BB????53CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
