rule _EXECryptor_2_2_x__SoftComplete_Developement_ezbteh
{
	meta:
		description = "EXECryptor 2_2_x __ SoftComplete Developement"
	strings:
		$a = {E8F7FEFFFF05????0000FFE0E8EBFEFFFF05????0000FFE0E804000000FFFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
