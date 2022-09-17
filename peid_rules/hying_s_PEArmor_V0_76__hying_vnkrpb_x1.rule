rule _hying_s_PEArmor_V0_76__hying_vnkrpb
{
	meta:
		description = "hying_s PEArmor V0_76 __ hying"
	strings:
		$a = {E90000000060E8140000005D81ED000000006A??E8A3000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
