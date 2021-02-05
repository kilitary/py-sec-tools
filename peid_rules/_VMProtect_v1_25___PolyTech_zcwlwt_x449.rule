rule __VMProtect_v1_25___PolyTech_zcwlwt
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5A9D5B5F5E5D585959C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
