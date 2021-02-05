rule __VMProtect_v1_25___PolyTech_vzpriu
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595B5E585D5F9D5A595FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
