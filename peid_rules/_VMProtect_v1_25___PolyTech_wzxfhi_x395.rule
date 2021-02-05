rule __VMProtect_v1_25___PolyTech_wzxfhi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A595D5D5A5F5E589D5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
