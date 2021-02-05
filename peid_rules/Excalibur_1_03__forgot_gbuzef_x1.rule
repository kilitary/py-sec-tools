rule _Excalibur_1_03__forgot_gbuzef
{
	meta:
		description = "Excalibur 1_03 __ forgot"
	strings:
		$a = {E90000000060E8140000005D81ED00000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
