rule __VMProtect_v1_25___PolyTech_ralqxr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC599D5D5A5B585F5E5E59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
