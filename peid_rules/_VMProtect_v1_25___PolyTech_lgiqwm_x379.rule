rule __VMProtect_v1_25___PolyTech_lgiqwm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC599D595A5F5E5D5D585BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
