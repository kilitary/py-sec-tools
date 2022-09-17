rule _CrunchPE_v5_0_boosee
{
	meta:
		description = "CrunchPE v5_0"
	strings:
		$a = {EB1503??????06}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
