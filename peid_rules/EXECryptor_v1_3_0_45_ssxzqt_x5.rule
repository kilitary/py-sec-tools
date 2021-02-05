rule _EXECryptor_v1_3_0_45_ssxzqt
{
	meta:
		description = "EXECryptor v1_3_0_45"
	strings:
		$a = {E81C008D9E4101403E8B961403B9EA0087DBF7D0311783C302E2F7C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
