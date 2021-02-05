rule _EXECryptor_V2_2X__softcomplete_com_aokhob
{
	meta:
		description = "EXECryptor V2_2X __ softcomplete_com"
	strings:
		$a = {FFE0E804000000FFFFFFFF5EC300}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
