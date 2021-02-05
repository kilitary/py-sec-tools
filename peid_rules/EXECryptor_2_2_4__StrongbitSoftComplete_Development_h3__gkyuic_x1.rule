rule _EXECryptor_2_2_4__StrongbitSoftComplete_Development_h3__gkyuic
{
	meta:
		description = "EXECryptor 2_2_4 __ StrongbitSoftComplete Development _h3_"
	strings:
		$a = {6B65726E656C33322E646C6C0000000000004765744D6F64756C6548616E646C6541000000004C6F61644C696272617279410000000047657450726F63416464726573730000000000004578697450726F63657373}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
