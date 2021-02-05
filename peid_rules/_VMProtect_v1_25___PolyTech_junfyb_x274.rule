rule __VMProtect_v1_25___PolyTech_junfyb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58585B5E5D585F9D595AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
