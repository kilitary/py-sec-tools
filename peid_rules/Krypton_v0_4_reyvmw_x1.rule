rule _Krypton_v0_4_reyvmw
{
	meta:
		description = "Krypton v0_4"
	strings:
		$a = {54E8????????5D8BC581ED6134????2B856037????83E806}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
