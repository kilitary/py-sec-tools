rule _AntiVirus_Vaccine_v_1_03_ttpwet
{
	meta:
		description = "AntiVirus Vaccine v_1_03"
	strings:
		$a = {FA33DBB9????0E1F33F6FCAD35????03D8E2}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
