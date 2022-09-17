rule __VMProtect_v1_25___PolyTech_debfxf
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B5A9D585F5E5E595DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
