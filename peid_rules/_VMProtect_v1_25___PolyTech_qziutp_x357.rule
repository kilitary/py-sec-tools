rule __VMProtect_v1_25___PolyTech_qziutp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595B9D5A5F59585D5E5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
