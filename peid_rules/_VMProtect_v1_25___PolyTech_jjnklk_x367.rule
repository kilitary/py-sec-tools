rule __VMProtect_v1_25___PolyTech_jjnklk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595E5D595B5A585F9D58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
