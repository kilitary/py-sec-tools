rule __VMProtect_v1_25___PolyTech_awdcpw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585D599D5D585B5E5A5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
