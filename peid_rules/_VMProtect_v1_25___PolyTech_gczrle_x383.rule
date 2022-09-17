rule __VMProtect_v1_25___PolyTech_gczrle
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC599D5A5F5D585B58595EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
