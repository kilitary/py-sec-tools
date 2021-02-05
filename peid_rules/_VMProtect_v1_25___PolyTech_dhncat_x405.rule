rule __VMProtect_v1_25___PolyTech_dhncat
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B585D589D595A5F5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
