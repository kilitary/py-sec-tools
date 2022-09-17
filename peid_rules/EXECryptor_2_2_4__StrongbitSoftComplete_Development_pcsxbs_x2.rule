rule _EXECryptor_2_2_4__StrongbitSoftComplete_Development_pcsxbs
{
	meta:
		description = "EXECryptor 2_2_4 __ StrongbitSoftComplete Development"
	strings:
		$a = {E8F7FEFFFF05????0000FFE0E8EBFEFFFF05????0000FFE0E8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
