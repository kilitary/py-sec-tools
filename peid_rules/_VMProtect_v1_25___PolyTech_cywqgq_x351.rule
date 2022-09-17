rule __VMProtect_v1_25___PolyTech_cywqgq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595A9D5E5D585F5A595BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
