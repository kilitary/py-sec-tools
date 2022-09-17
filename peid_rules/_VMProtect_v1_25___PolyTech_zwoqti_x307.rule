rule __VMProtect_v1_25___PolyTech_zwoqti
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585B9D595E5D5D5F5A58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
