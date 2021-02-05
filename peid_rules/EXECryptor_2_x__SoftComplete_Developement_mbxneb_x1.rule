rule _EXECryptor_2_x__SoftComplete_Developement_mbxneb
{
	meta:
		description = "EXECryptor 2_x __ SoftComplete Developement"
	strings:
		$a = {A4????0000000000FFFFFFFF3C????0094????00D8????0000000000FFFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
