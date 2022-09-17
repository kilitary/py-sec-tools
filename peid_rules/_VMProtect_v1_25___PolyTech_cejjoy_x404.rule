rule __VMProtect_v1_25___PolyTech_cejjoy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B585A595E9D5E5D5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
