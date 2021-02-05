rule __VMProtect_v1_25___PolyTech_cjekxh
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595B5F5E589D5D5A5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
