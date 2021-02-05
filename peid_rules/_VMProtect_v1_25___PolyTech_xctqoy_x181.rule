rule __VMProtect_v1_25___PolyTech_xctqoy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A066698988D760183ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
