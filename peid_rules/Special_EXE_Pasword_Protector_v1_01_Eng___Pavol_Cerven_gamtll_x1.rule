rule _Special_EXE_Pasword_Protector_v1_01_Eng___Pavol_Cerven_gamtll
{
	meta:
		description = "Special EXE Pasword Protector v1_01 _Eng_ __ Pavol Cerven"
	strings:
		$a = {60E8000000005D81ED0600000089AD8C0100008BC52B85FE75000089853E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
