rule __VMProtect_v1_25___PolyTech_jzgqpq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595A5E589D5D585B5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
