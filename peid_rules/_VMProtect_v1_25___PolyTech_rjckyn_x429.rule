rule __VMProtect_v1_25___PolyTech_rjckyn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5F5B9D5D5A5E585A59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
