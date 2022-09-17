rule __VMProtect_v1_25___PolyTech_auibnb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59595A9D5E585F5D595BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
