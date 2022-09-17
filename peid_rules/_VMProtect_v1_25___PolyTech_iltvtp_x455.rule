rule __VMProtect_v1_25___PolyTech_iltvtp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5D5A5F589D5E5B5958C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
