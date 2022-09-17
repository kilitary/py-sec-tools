rule _RLPack_V1_18_Basic_Edition_aPlib_0_43___ap0x_ntpsuk
{
	meta:
		description = "RLPack V1_18 Basic Edition _aPlib 0_43_  __ ap0x"
	strings:
		$a = {60E8000000008B2C2483C4048DB51A0400008D9DC102000033FFE861010000EB0FFF74}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
