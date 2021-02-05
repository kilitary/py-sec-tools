rule __VMProtect_v1_25___PolyTech_mfathr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B585D5E5F9D5A595AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
