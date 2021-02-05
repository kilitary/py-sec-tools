rule _RLPack_1_1_BasicEdition__ap0x_napolq
{
	meta:
		description = "RLPack 1_1 BasicEdition __ ap0x"
	strings:
		$a = {60E8000000008B2C2483C4048DB54A0200008D9D1101000033FFEB0FFF743704FF3437FFD383C40883C708833C370075EB8D743704536A40680010000068}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
