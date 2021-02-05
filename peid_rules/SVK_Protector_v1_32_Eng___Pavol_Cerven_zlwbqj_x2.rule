rule _SVK_Protector_v1_32_Eng___Pavol_Cerven_zlwbqj
{
	meta:
		description = "SVK Protector v1_32 _Eng_ __ Pavol Cerven"
	strings:
		$a = {60E8000000005D81ED06000000EB05B80636420064A023}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
