rule _Special_EXE_Password_Protector_1_0__Pavol_Cerven_eegyxy
{
	meta:
		description = "Special EXE Password Protector 1_0 __ Pavol Cerven"
	strings:
		$a = {60E8000000005D81ED0600000089AD8C0100008BC52B85FE75000089853E77}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
