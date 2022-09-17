rule __VMProtect_v1_25___PolyTech_rsqifr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB6068D760166989883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
